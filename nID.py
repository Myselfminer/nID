class nIDError(Exception):
    def __init__(self,value):
        self.value=value
    def __str__(self):
        return repr(self.value)
def count(list):
    counter=0
    for i in list:
        counter=counter+1
    return counter
def parse(nid,field):
    try:
        split=nid.split("@")
        count=0
        loop=0
        output=""
        for i in field:
            count=count+1
        for i in split:
            if i.startswith(field):
                for u in i:
                    if loop <= count:
                        pass
                    else:
                        output=output+u
                    loop=loop+1
        return output
    except:
        raise nIDError("Could not Parse nid")
def field_from_table(nid, field, row_field_name, row_field_value, api=2):
    to_return=False
    if api >= 2:
        split_row1=nid.split("\n")#Split Rows
        for i in split_row1:#Search Header Data
            b=i.split("$")#Split Header and Data
            if count(b) < 2:#Raise Error if more than one header was detected
                raise nIDError("At least 1 Nid contains more than one header.")
            fields=b[0].split("@")#Split Tags of the Header
            for u in fields:
                final=u.split(":")#Split Tag and Value
                if final[0]==row_field_name:#search tag name
                    if final[1]==row_field_value:#compare header value
                        final_fields=b[1].split("@")#split data
                        for r in final_fields:#         | Search |
                            really_final=r.split(":")#  |  field |
                            if really_final[0]==field:#check field
                                to_return=really_final[1]
    if to_return != False:
        return to_return
    else:
        raise nIDError("Could not find field(s)")

