class UniTeller():
    def __init__(self):
        # for reading data
        filename ="C:\\Users\Senkrish\Downloads\Columbia Studies\Fall\Big Data Analytics/MERGED2013_PP.csv"
        data = open(filename)

        # get columns
        cols = data.readline().strip().split(',')

        # get all the indices
        uni_code = cols.index("opeid6")
        ind1 = cols.index('NPT41_PUB')## finance
        ind2 = cols.index('NPT42_PUB')
        ind3 = cols.index('NPT43_PUB')
        ind4 = cols.index('NPT44_PUB')
        ind5 = cols.index('NPT45_PUB')
        ind6 = cols.index('NPT41_PRIV')
        ind7 = cols.index('NPT42_PRIV')
        ind8 = cols.index('NPT43_PRIV')
        ind9 = cols.index('NPT44_PRIV')
        ind10 = cols.index('NPT45_PRIV')
        ind11 = cols.index('SAT_AVG_ALL')
        ind12 = cols.index('ADM_RATE_ALL')
        ind13 = cols.index('INSTNM') # institute name

        list_ind = [ind1, ind2, ind3, ind4, ind5, ind6,\
        ind7, ind8, ind9, ind10]

        inds= {
        ind1: ["income1", "public"],
        ind2: ["income2", "public"],
        ind3: ["income3", "public"],
        ind4: ["income4", "public"],
        ind5: ["income5", "public"],
        ind6: ["income1", "private"],
        ind7: ["income2", "private"],
        ind8: ["income3", "private"],
        ind9: ["income4", "private"],
        ind10: ["income5", "private"]
        }
        # setup data sctructure

        ## store data here
        university = {}


        # finance
        financial_information = {
        'income1': { 'private': [], 'public': []},
        "income2":  { 'private': [], 'public': []},
        'income3': { 'private': [], 'public': []},
        "income4":  { 'private': [], 'public': []},
        'income5': { 'private': [], 'public': []},
        }


        for line in data:
            row = line.strip().split(',')
            # FINANCIAL INFORMATION
            for x in list_ind:
                if row[x] != "NULL":
                    income_level = inds[x][0]
                    pub_priv = inds[x][1]
                    financial_information[income_level][pub_priv].append((row[uni_code], int(row[x])))
            # UNIVERSITY INFORMATION
            if row[ind11] != "NULL":
                university[row[uni_code]] = {'SAT': int(row[ind11]), 'admission_rate': float(row[ind12]), "name": row[ind13]}
            else:
                university[row[uni_code]] = {'SAT': 0, 'admission_rate': 1, "name": row[ind13]}

            self.financial_information = financial_information
            self.university = university

    def getUnis(self, income, priv_public, afford, sat):
        if priv_public == 0:
            priv_public = "public"
        else:
            priv_public = "private"
        list_of_unis = self.financial_information[getIncomeLevel(income)][priv_public]
        output = []
        for uni in list_of_unis:
            if afford >= int(uni[1]):
                output.append(uni)

        # sat/act
        # assuming we are using sat
        final_output = []
        for i in output:
            if sat > self.university[i[0]]['SAT']:
                final_output.append(i)

        top10 = sorted(final_output, key=lambda x: self.university[x[0]]['admission_rate'])[:10]
        out = []
        for x in top10:
            out.append({"NAME" : self.university[x[0]]['name'], 'Admission Rate': self.university[x[0]]['admission_rate']})
        return out

# filter by financial INFORMATION
def getIncomeLevel(income):
    if income>0 and income<=30000:
        return "income1"
    if income>30000 and income<=48000:
        return "income2"
    if income>48000 and income<=75000:
        return "income3"
    if income>75000 and income<=110000:
        return "income4"
    return "income5"
#
# ## student inputting his scores and financnial INFORMATION
# income = 20000
# priv_public= "public"
# afford = 5000
# sat = 2300
#

if __name__ == "__main__":
    teller = UniTeller()

    income = int(input("Please enter your annual family income: "))
    priv_public = int(input("Enter preference of Private(1) & Public(0) institutions: "))
    afford = int(input("Please enter your annual budget for education: "))
    sat = int(input("Please enter your SAT score :"))

    output = teller.getUnis(income, priv_public, afford, sat)
    print(output)
