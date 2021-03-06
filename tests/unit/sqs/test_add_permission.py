#!/usr/bin/env python
# Copyright 2012-2013 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import unittest
import awscli.clidriver


class TestAddPermission(unittest.TestCase):

    def setUp(self):
        self.driver = awscli.clidriver.CLIDriver()
        self.prefix = 'aws sqs add-permission'
        self.queue_url = 'https://queue.amazonaws.com/4444/testcli'

    def test_all_param(self):
        cmdline = self.prefix
        cmdline += ' --queue-url %s' % self.queue_url
        cmdline += ' --aws-account-ids 888888888888'
        cmdline += ' --actions SendMessage'
        cmdline += ' --label FooBarLabel'
        result = {'QueueUrl': self.queue_url,
                  'ActionName.1': 'SendMessage',
                  'AWSAccountId.1': '888888888888',
                  'Label': 'FooBarLabel'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)

    def test_multiple_accounts(self):
        cmdline = self.prefix
        cmdline += ' --queue-url %s' % self.queue_url
        cmdline += ' --aws-account-ids 888888888888 999999999999'
        cmdline += ' --actions SendMessage'
        cmdline += ' --label FooBarLabel'
        result = {'QueueUrl': self.queue_url,
                  'ActionName.1': 'SendMessage',
                  'AWSAccountId.1': '888888888888',
                  'AWSAccountId.2': '999999999999',
                  'Label': 'FooBarLabel'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)

    def test_multiple_actions(self):
        cmdline = self.prefix
        cmdline += ' --queue-url %s' % self.queue_url
        cmdline += ' --aws-account-ids 888888888888'
        cmdline += ' --actions SendMessage ReceiveMessage'
        cmdline += ' --label FooBarLabel'
        result = {'QueueUrl': self.queue_url,
                  'ActionName.1': 'SendMessage',
                  'ActionName.2': 'ReceiveMessage',
                  'AWSAccountId.1': '888888888888',
                  'Label': 'FooBarLabel'}
        params = self.driver.test(cmdline)
        self.assertEqual(params, result)


if __name__ == "__main__":
    unittest.main()
