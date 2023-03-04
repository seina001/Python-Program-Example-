#!/usr/bin/env python
"""Information on what your package does.
ChevLab_add adds together two numbers by putting them into a pandas dataframe and summing the contents. Why you might ask?

Because we can.

But also to show how to import dependencies and packages for your own package.

Usage:
chevlab_add --first_num (required) --second_num (required) --divide_by_two (optional, TRUE or FALSE) --log (logfile, default is logfile.log)

Citation:
Einarsson 2023, Science, Vol: 3.6.23
"""

import argparse
import logging
import time
import os
import math
import pandas as pd

def myparser():
    parser = argparse.ArgumentParser(description='chevlabpkg adds together two numbers by putting them into a pandas dataframe and summing the contents. Optionally divides by 2.')
    parser.add_argument('--first_num', '-f', type=float, required=True,
                        help='Put a first number, thats all.')
    parser.add_argument('--second_num', '-s', type=float, required=True,
                        help='Put a second number, thats all.')
    parser.add_argument('--divide_by_two', '-d2', type=bool, default=False,
                        help='True or False, if you want to divide the total by 2')
    parser.add_argument('--log' ,help="Logfile, default is logfile.log", default="logfile.log")
    return parser

class DataframeInit:
    """Class for adding two numbers into a pandas dataframe and checking validity.

    Args:
        num1 (float):  Numero uno
        num2 (float):  Numero dos
    """
    def _create_dataframe(num1, num2):
        """Initializes dataframe and adds numbers to a column.

        Args:
            num1: Number 1 (float)
            num2: Number 2 (float)
        """
        dataf = pd.DataFrame()
        dataf['Numbers'] = [num1, num2]
        return dataf
    
    def _check_input(num1,num2):
        """Check if the numbers aren't digits.
        Args:
            num1: number one
            num2: number two
        """
        try:
            total = num1+num2
        except TypeError as e:
            logging.error("One of your numbers is not a number")
            raise e

class AdditionDivision:
    """Class for adding two numbers into a pandas dataframe and checking validity.

    Args:
        dataf (df): Pandas dataframe.
        sum (float): Sum of the two numbers.

    Attributes:
        sum: Sums up the values in the dataframe

    """
    def _sumdataframe(dataf):
        sum = dataf.sum()
        return sum
    
    def _divide(sum):
        half_sum = sum/2
        return half_sum
    
def _logger_setup(logfile):
    """Set up logging to a logfile and the terminal standard out.
    Args:
        logfile: logfile default is logfile.log. Use --log if you want to change logfile name.
    """
    try:
        logging.basicConfig(level=logging.DEBUG,
                            format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                            datefmt='%m-%d %H:%M',
                            filename=logfile,
                            filemode='w')
        # define a Handler which writes INFO messages or higher to the sys.stderr
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        # set a format which is simpler for console use
        formatter = logging.Formatter('%(asctime)s: %(levelname)-8s %(message)s')
        # tell the handler to use this format
        console.setFormatter(formatter)
        # add the handler to the root logger
        #logging.getLogger('').addHandler(console)
    except Exception as e:
        print("An error occurred setting up logging")
        raise e

def main(args=None):
    """Run complete workflow for this program.

    """
    t0 = time.time()
    parser = myparser()
    if not args:
        args = parser.parse_args()
    _logger_setup(args.log)
    try:
        logging.info("Checking input.")
        DataframeInit._check_input(args.first_num, args.second_num)
        logging.info("Initializing and adding to dataframe.")
        dataframe = DataframeInit._create_dataframe(args.first_num, args.second_num)
        sum_nrs = AdditionDivision._sumdataframe(dataframe)
        print(args.first_num," + ", args.second_num," = ", sum_nrs[0] )
        if (args.divide_by_two):
            sum_divided = AdditionDivision._divide(sum_nrs)
            print(sum_nrs[0], " \ 2 = ", sum_divided[0]  )
            logging.info("Dividing numbers.")
        t1 = time.time()
        fmttime = time.strftime("%H:%M:%S", time.gmtime(t1-t0))
        logging.info("ChevLab_add ran in {}".format(fmttime))
    except Exception as e:
        logging.error("ChevLab_add terminated with errors. See the log file for details.")
        logging.error(e)
        raise SystemExit(1)


if __name__ == '__main__':
    main()
