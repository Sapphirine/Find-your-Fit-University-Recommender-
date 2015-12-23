from pyspark.sql import HiveContext
from pyspark import SparkContext
import sys
import getopt

# Get list of recommended universities sorted by admisstion rate 
def getUniversities(income, school_type, afford, sat):
    sc = SparkContext("local", "Simple App")
    sqlContext = HiveContext(sc)
    col_name = getColumnName(income, school_type)
    results = sqlContext.sql("SELECT inst_name, adm_rate_all, sat_avg_all, %s as estimated_cost FROM school_admit_data where sat_avg_all <= %s and %s <= %s order by adm_rate_all DESC limit 10" % (col_name,sat,col_name,afford)).collect()
    print ("Computing recommendations for: annual income %s, school type %s, amount that can be spent on school %s, sat score %s" %(income,school_type,afford,sat))
    print ("%50s\tAVG.SAT SCORE\tESTIMATED COST\tADMISSION RATE" %('INSTITUTE'))
    for result in results:
	print ("%50s\t\t%d\t\t%d\t\t%0.2f" %(result.inst_name, result.sat_avg_all,result.estimated_cost,result.adm_rate_all))

	
# Get column name corresponsing to income level and school type 
def getColumnName(income, school_type):
    income_level = getIncomeLevelCode(income)
    col_name = "npt"+income_level+"_"+school_type
    return col_name

# filter by financial INFORMATION
def getIncomeLevelCode(income):
    if income>0 and income<=30000:
        return "41"
    if income>30000 and income<=48000:
        return "42"
    if income>48000 and income<=75000:
        return "43"
    if income>75000 and income<=110000:
        return "44"
    return "45"

#
# Usage: ./bin/spark-submit RecommendSchool.py -i <income> -t <school_type> -a <can_afford> -s <sat_score>'
#
if __name__ == "__main__":
	# income = '0'
	# school_type = 'pub' 
	# afford = '0'
	# sat = '0'
	opts, args = getopt.getopt(sys.argv[1:],"hi:t:a:s:",['help','income=','school_type=','can_afford=','sat_score='])
	for opt, arg in opts:
      		if opt == '-h':
         		print './bin/spark-submit RecommendSchool.py -i <income> -t <school_type> -a <can_afford> -s <sat_score>'
         		sys.exit()
      		elif opt in ("-i","--income"):
			print "Parsing income"
         		income = arg
      		elif opt in ("-t","--school_type"):
         		school_type = arg
		elif opt in ("-a","--can_afford"):
			afford = arg
		elif opt in ("-s","--sat_score"):
			sat = arg

	getUniversities(income, school_type, afford, sat)

