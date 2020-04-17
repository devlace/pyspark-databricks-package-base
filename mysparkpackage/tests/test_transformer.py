#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `ddo_transform` package."""

import pytest
import os
from mysparkpackage.core import transformer
from pyspark.sql import DataFrame


@pytest.fixture
def spark():
    """Spark Session fixture"""
    from pyspark.sql import SparkSession

    spark = SparkSession.builder\
        .master("local[2]")\
        .appName("Unit Testing")\
        .getOrCreate()
    spark.sparkContext.setLogLevel("ERROR")
    return spark


def test_standardize(spark):
    """Test data transform"""
    # Arrange
    my_df = spark.read.format("csv").load("./data/iris.csv")
    # Act
    transformed_df = transformer.transform(my_df)
    # Assert
    assert transformed_df.count() == 151