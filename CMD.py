from __future__ import division, print_function, absolute_import

# import os

import glob
from SortGiantPileofSpreadsheets import assign_id

from astropy.table import Table, Column
import matplotlib.pyplot as plt


def __init__(self, tstuff):
    self.__stuff = tstuff


def make_CMD(short_w_file, long_w_file):
    """Links the two data sets it is given so the RA/Decs agree and plots a CMD.

    Compares second data set to first data set and assigns second data set the
    DataNum of first data set where the RA and Dec columns are within a
    reasonable range.  Uses function from another module to do so.  Removes the
    points not in both data sets so they can be ploted together and creates a
    CM Diagram of the data.

    Parameters
    ------
    short_w_file, long_w_file: filename
    short_wave, long_wave: list
    short_w, long_w: astropy table

    """
    short_wave = glob.glob(short_w_file)
    short_w = Table.read(short_wave[0])
    long_wave = glob.glob(long_w_file)
    long_w = Table.read(long_wave[0])

    # send through matching function in Sort module to make the DataNum's match
    long_w = assign_id(short_w, long_w, 'AvgRA', 'AvgDec')

    #print(long_w["DataNum", "AvgRA"], short_w["DataNum", "AvgRA"])
    short_w = match(short_w, long_w)
    #long_w = match(long_w, short_w)
    #print(long_w["DataNum", "AvgRA"], short_w["DataNum", "AvgRA"])

    # plot short - long vs instrumental mag
    plt(short_w["AvgFlux"]-long_w["AvgFlux"], short_w["InstruMag"])


def match(first, second):
    """Finds which items are in both data sets.

    Creates a list of True/False for whether the items of the first data set
    are in the second data set. Returns only the items of the first data set
    that are in the second data set.

    Parameters
    ------
    first, second: astropy table
    first_list, second_list: list
    matches: list

    Returns
    ------
    first: astropy table
    """

    matches = []
    first_list = list(first["DataNum"])
    second_list = list(second["DataNum"])
    for i in first_list:
        if i in second_list:
            matches.append(True)
        else:
            matches.append(False)
    #print(len(matches))
    print(first["DataNum", "AvgRA"])
    first = first[matches] ####this isn't working do I need to make it an array instead or......
    print(first["DataNum", "AvgRA"])
    #print(len(matches))
    return first
