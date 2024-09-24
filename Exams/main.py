from db import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

db = Database(database="local", collection="exam_1")
motoristaDao = MotoristaDAO(database=db)

motoristaCLI = MotoristaCLI(motoristaDao)
motoristaCLI.run()
