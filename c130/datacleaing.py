import csv
import pandas as pd

data_file = pd.read_csv("c130/final.csv")

# to dispaly rows and columns of csv file 
print(data_file.shape)

# to remove a column from the csv file
del data_file["pl_orbpererr1"]
print(data_file.shape)

# to dispaly the column names 
print(list(data_file))

# to rename a column in csv file 
data_file = data_file.rename({"pl_hostname":"solar_system_name",},axis="columns")
print(list(data_file))


# write the changes in a new csv file 

del data_file["hyperlink"]
del data_file["temp_planet_date"]
del data_file["temp_planet_mass"]
del data_file["pl_letter"]
del data_file["pl_name"]
del data_file["pl_controvflag"]
del data_file["pl_pnum"]
del data_file["pl_orbper"]
del data_file["pl_orbpererr1"]
del data_file["pl_orbpererr2"]
del data_file["pl_orbperlim"]
del data_file["pl_orbsmax"]
del data_file["pl_orbsmaxerr1"]
del data_file["pl_orbsmaxerr2"]
del data_file["pl_orbsmaxlim"]
del data_file["pl_orbeccen"]
del data_file["pl_orbeccenerr1"]
del data_file["pl_orbeccenerr2"]
del data_file["pl_orbeccenlim"]
del data_file["pl_orbinclerr1"]
del data_file["pl_orbinclerr2"]
del data_file["pl_orbincllim"]
del data_file["pl_bmassj"]
del data_file["pl_bmassjerr1"]
del data_file["pl_bmassjerr2"]
del data_file["pl_bmassjlim"]
del data_file["pl_bmassprov"]
del data_file["pl_radj"]
del data_file["pl_radjerr1"]
del data_file["pl_radjerr2"]
del data_file["pl_radjlim"]
del data_file["pl_denserr1"]
del data_file["pl_denserr2"]
del data_file["pl_denslim"]
del data_file["pl_ttvflag"]
del data_file["pl_kepflag"]
del data_file["pl_k2flag"]
del data_file["pl_nnotes"]
del data_file["ra"]
del data_file["dec"]
del data_file["st_dist"]
del data_file["st_disterr1"]
del data_file["st_disterr2"]
del data_file["st_distlim"]
del data_file["gaia_dist"]
del data_file["gaia_disterr1"]
del data_file["gaia_disterr2"]
del data_file["gaia_distlim"]
del data_file["st_optmag"]
del data_file["st_optmagerr"]
del data_file["st_optmaglim"]
del data_file["st_optband"]
del data_file["gaia_gmag"]
del data_file["gaia_gmagerr"]
del data_file["gaia_gmaglim"]
del data_file["st_tefferr1"]
del data_file["st_tefferr2"]
del data_file["st_tefflim"]
del data_file["st_masserr1"]
del data_file["st_masserr2"]
del data_file["st_masslim"]
del data_file["st_raderr1"]
del data_file["st_raderr2"]
del data_file["st_radlim"]
del data_file["rowupdate"]
del data_file["pl_facility"]

data_file = data_file.rename({
                'pl_hostname': "solar_system_name", 
                'pl_discmethod': "planet_discovery_method", 
                'pl_orbincl': "planet_orbital_inclination", 
                'pl_dens': "planet_density", 
                'ra_str': "right_ascension", 
                'dec_str': "declination", 
                "st_teff": "host_temperature", 
                'st_mass': "host_mass", 
                'st_rad': "host_radius"
            }, axis='columns')

data_file.to_csv('data_cleaned_file.csv') 


# to check if the csv file has the correct data
# df = pd.read_csv("c130/data_cleaned_file.csv")
# print(df.shape)
# print(list(df))