import Script_fetch_from_db
import Parse
import process
import dataprocess
import laggeddata
import weatherunion_script
import model_predict

print("Script_fetch_from_db ...")
Script_fetch_from_db.run()

# Execute script2
print("Parse script...")
Parse.run()

print("process script...")
process.run()

# Execute script2
print("dataprocess script...")
dataprocess.run()

print("laggeddata script...")
laggeddata.run()

# Execute script2
print("weatherunion_script script...")
weatherunion_script.run()

print("model_predict script...")
model_predict.run()

print("model_predict script...")
app.run()




