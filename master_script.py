import Script_fetch_from_db
import Parse
import process
import dataprocess
import laggeddata
import weatherunion_script
import model_predict

Script_fetch_from_db.run()

# Execute script2
Parse.run()

Process.run()

# Execute script2
dataprocess.run()

laggeddata.run()

# Execute script2
weatherunion_script.run()

model_predict.run()

app.run()




