from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from automatedpbtfalsepython.config.ConfigStore import *
from automatedpbtfalsepython.udfs.UDFs import *

def Script_1(spark: SparkSession, in0: DataFrame) -> DataFrame:
    print("Successfully Executed Son.")
    out0 = in0

    return out0
