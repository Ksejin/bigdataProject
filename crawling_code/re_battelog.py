#battlelog테이블 중복제거, re_battlelog테이블 생성
import DB_connection


conn = DB_connection.engine.connect()
drop_reBattlelog = conn.execute("DROP TABLE IF EXISTS re_battlelog")
create_reBattlelog = conn.execute("create table re_battlelog select distinct * from battlelog")
turncate_battlelog = conn.execute("Truncate battlelog")
conn.close()
