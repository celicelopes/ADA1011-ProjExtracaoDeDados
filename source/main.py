from connectNewsAPI import connectNewsApi
from saveData import saveData, printData

saveData(connectNewsApi())
printData()