#!/usr/bin/python
#coding=utf-8

import sys
import getopt
import argparse

import tushare as ts


def main(args):
	print("--address {0}".format(args.history_time))    #args.address会报错，因为指定了dest的值
	print("--stock {0}".format(args.stock))    #args.address会报错，因为指定了dest的值

	stock=args.stock


	ts.get_hist_data(stock) #一次性获取全部日k线数据
	
	


if __name__ == '__main__':
	parser = argparse.ArgumentParser(usage="it's usage tip.", description="help info.")
	parser.add_argument("-ht","--history_time", default=3,help="the history of the stock")
	parser.add_argument("-n","--stock", default=0,required=True,help="the stock number, zero for all")
	args = parser.parse_args()
	main(args)

