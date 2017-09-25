import json
import os
from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy import text


app = Flask(__name__)
def getDbAddress():
    if 'DPP_DB_ENGINE' in os.environ:
        return os.environ['DPP_DB_ENGINE'];
    return 'postgresql://postgres:123456@localhost:15432/postgres'

eng = create_engine(getDbAddress())

@app.route("/")
def hello():
    inspector = inspect(eng)
    s = "";
    for table_name in inspector.get_table_names():
      s += "<p> Table name: %s <br/>" % table_name
      for column in inspector.get_columns(table_name):
        s += ("Column: %s <br/>" % column['name'])
      s += "</p>"
    return s;
    
@app.route("/commitees")
def commitees():
    sql = text('select kns_committee."CommitteeID", kns_committee."Name", kns_committee."ParentCommitteeID", kns_committee."CommitteeParentName" from kns_committee')
    result = eng.execute(sql)
    s = "<table dir='rtl'>"
    s+= "<tr><td>Name</td><td>Id</td><td>ParentName></td><td>ParentId</td>"
    for row in result:
        name = str(row[1]);
        num = str(row[0]);
        parentNum = str(row[2])
        parentName = str(row[3])
        s += "<tr><td>" + str(row[1]) + "</td><td>" + num + "</td><td>" + parentName + "</td><td>" + parentNum + "</td></tr>" 
    s+="</table>";
    return s;
    
@app.route("/commitee/childof/<commitee_id>")
def commitee(commitee_id):
    sql = text('select kns_committee."CommitteeID", kns_committee."Name"  from kns_committee WHERE kns_committee."ParentCommitteeID"=' + str(commitee_id))

    result = eng.execute(sql)
    s = "<table dir='rtl'>"
    for row in result:
        name = str(row[1]);
        num = str(row[0]);
        s += "<tr><td>" + str(row[1]) + "</td><td>" + num + "</td></tr>"
    s+="</table>";
    return s;
    
@app.route("/commiteeNames")
def commiteeNames():
    sql = text('select kns_committee."CommitteeID" as id, kns_committee."Name" as name from kns_committee order by name ASC;')
    rows = eng.execute(sql)
    result = {row[1]:row[0] for row in rows}
    return json.dumps(result);
    

