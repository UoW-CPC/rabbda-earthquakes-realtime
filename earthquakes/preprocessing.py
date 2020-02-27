

class Preprocessing:

    @classmethod
    def cleanHeaders(cls, eq_list_raw):
        eq_list_temp = []
        for eq in eq_list_raw:
            if 'time' in eq:
                print "response headers removed"
            else:
                eq_list_temp.append(eq)
        return eq_list_temp

    @classmethod
    def splitDateTime(cls, eq_list_temp):
        eq_list = []
        for eq in eq_list_temp:
            eq_temp = eq
            eq_str = "".join(eq)
            eq_year = eq_str[0:4]
            eq_temp.insert(0,eq_year)
            eq_month = eq_str[5:7]
            eq_temp.insert(1,eq_month)
            eq_day = eq_str[8:10]
            eq_temp.insert(2, eq_day)
            eq_time = eq_str[11:19]
            eq_temp.insert(3, eq_time)
            eq_list.append(eq_temp)
        return eq_list

