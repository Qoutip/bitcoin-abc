#!/usr/bin/env python3
# Copyright (c) 2022 The Bitcoin developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_framework.netutil import test_ipv6_local
from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import assert_equal


class ChronikServeTest(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = True
        self.num_nodes = 1
        self.extra_args = [["-chronik"]]

    def skip_test_if_missing_module(self):
        self.skip_if_no_chronik()

    def run_test(self):
        from test_framework.chronik.client import ChronikClient

        def test_host(ip, port):
            chronik = ChronikClient(ip, port)
            response = chronik._request_get("/path/does/not/exist", pb_type=None)
            assert_equal(response.err(404).msg, "404: Not found: /path/does/not/exist")

        test_host("127.0.0.1", self.nodes[0].chronik_port)

        self.restart_node(0, ["-chronik", "-chronikbind=0.0.0.0"])
        test_host("127.0.0.1", 18442)

        self.restart_node(0, ["-chronik", "-chronikbind=127.0.0.1:12345"])
        test_host("127.0.0.1", 12345)

        if test_ipv6_local():
            self.restart_node(
                0,
                [
                    "-chronik",
                    "-chronikbind=127.0.0.1:12345",
                    "-chronikbind=[::1]:23456",
                ],
            )
            test_host("127.0.0.1", 12345)
            test_host("::1", 23456)


if __name__ == "__main__":
    ChronikServeTest().main()
