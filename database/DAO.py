from database.DB_connect import DBConnect
from model.confine import Confine
from model.country import Country


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getAllNazioni(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary = True)
        query= """SELECT c.StateAbb, c.CCode, c.StateNme
                FROM country c, contiguity cc
                WHERE (c.CCode=cc.state1no or c.CCode=cc.state2no) and cc.`year` <= %s AND cc.conttype = 1
                GROUP BY c.StateAbb, c.CCode, c.StateNme
                """

        cursor.execute(query,(anno,))
        nazioni = []
        for row in cursor:
            nazioni.append(Country(**row))

        cursor.close()
        cnx.close()
        return nazioni

    @staticmethod
    def getAllConfini(anno):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor(dictionary=True)
        query = """SELECT cc.state1no, cc.state2no
                FROM country c, contiguity cc
                WHERE (c.CCode=cc.state1no or c.CCode=cc.state2no) and cc.`year` <= %s and conttype =1
                GROUP BY cc.state1no, cc.state2no 
                """

        cursor.execute(query, (anno,))
        confini = []
        for row in cursor:
            confini.append(Confine(**row)) #senza Cofine hogia le tuple

        cursor.close()
        cnx.close()
        return confini