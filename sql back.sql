-- ************************************************************************************************************************************************
-- ENTRADA
CREATE OR REPLACE VIEW vw_pase_direccion AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 7;

ALTER TABLE vw_pase_direccion
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_direccion DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_direccion DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 7, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_direccion DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 7 AND seguimiento_pase.idpase = old.idpase;

-- SALIDA

CREATE OR REPLACE VIEW vw_pase_direccion_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 7;

ALTER TABLE vw_pase_direccion_s
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_direccion_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_direccion_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 7, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_direccion_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.origen = 7 AND seguimiento_pase.idpase = old.idpase;

-- ************************************************************************************************************************************************
-- ENTRADA
CREATE OR REPLACE VIEW vw_pase_lic_com AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 5;

ALTER TABLE vw_pase_lic_com
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_lic_com DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_lic_com DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 5, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_lic_com DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 5 AND seguimiento_pase.idpase = old.idpase;

--SALIDA

CREATE OR REPLACE VIEW vw_pase_lic_com_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 5;

ALTER TABLE vw_pase_lic_com_s
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_lic_com_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_lic_com_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 5, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_lic_com_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.origen = 5 AND seguimiento_pase.idpase = old.idpase;

-- ************************************************************************************************************************************************
-- ENTRADA

CREATE OR REPLACE VIEW vw_pase_mesa_ent AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 3;

ALTER TABLE vw_pase_mesa_ent
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_mesa_ent DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_mesa_ent DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 3, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_mesa_ent DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 3 AND seguimiento_pase.idpase = old.idpase;

-- SALIDA

CREATE OR REPLACE VIEW vw_pase_mesa_ent_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 3;

ALTER TABLE vw_pase_mesa_ent_s
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_mesa_ent_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_mesa_ent_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 3, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_mesa_ent_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.origen = 3 AND seguimiento_pase.idpase = old.idpase;

-- ************************************************************************************************************************************************
-- ENTRADA
CREATE OR REPLACE VIEW vw_pase_otros AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 1;

ALTER TABLE vw_pase_otros
  OWNER TO postgres;



CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_otros DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_otros DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 1, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_otros DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 1 AND seguimiento_pase.idpase = old.idpase;

-- SALIDA

CREATE OR REPLACE VIEW vw_pase_otros_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 1;

ALTER TABLE vw_pase_otros_s
  OWNER TO postgres;



CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_otros_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_otros_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 1, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_otros_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.origen = 1 AND seguimiento_pase.idpase = old.idpase;

-- ************************************************************************************************************************************************
-- ENTRADA

CREATE OR REPLACE VIEW vw_pase_patrimonio AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 6;

ALTER TABLE vw_pase_patrimonio
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_patrimonio DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_patrimonio DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 6, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_patrimonio DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 6 AND seguimiento_pase.idpase = old.idpase;

-- SALIDA

CREATE OR REPLACE VIEW vw_pase_patrimonio_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 6;

ALTER TABLE vw_pase_patrimonio_s
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_patrimonio_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_patrimonio_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 6, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_patrimonio_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.origen = 6 AND seguimiento_pase.idpase = old.idpase;

-- ************************************************************************************************************************************************
--ENTRADA
CREATE OR REPLACE VIEW vw_pase_presupuesto AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 4;

ALTER TABLE vw_pase_presupuesto
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_presupuesto DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_presupuesto DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 4, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_presupuesto DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 4 AND seguimiento_pase.idpase = old.idpase;

--SALIDA

CREATE OR REPLACE VIEW vw_pase_presupuesto_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 4;

ALTER TABLE vw_pase_presupuesto_s
  OWNER TO postgres;


CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_presupuesto_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_presupuesto_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 4, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_presupuesto_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.origen = 4 AND seguimiento_pase.idpase = old.idpase;

-- ************************************************************************************************************************************************
-- ENTRADA

CREATE OR REPLACE VIEW vw_pase_tesoreria AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.destino = 2;

ALTER TABLE vw_pase_tesoreria
  OWNER TO postgres;

CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_tesoreria DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_tesoreria DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, new.origen, 2, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_tesoreria DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 2 AND seguimiento_pase.idpase = old.idpase;

-- SALIDA

CREATE OR REPLACE VIEW vw_pase_tesoreria_s AS 
 SELECT seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido
   FROM seguimiento_pase
  WHERE seguimiento_pase.origen = 2;

ALTER TABLE vw_pase_tesoreria_s
  OWNER TO postgres;

CREATE OR REPLACE RULE "_DELETE" AS
    ON DELETE TO vw_pase_tesoreria_s DO INSTEAD  DELETE FROM seguimiento_pase
  WHERE seguimiento_pase.idpase = old.idpase;


CREATE OR REPLACE RULE "_INSERT" AS
    ON INSERT TO vw_pase_tesoreria_s DO INSTEAD  INSERT INTO seguimiento_pase (documento, fecha_ing, motivo, envio, origen, destino, recepcion, observacion, recibido) 
  VALUES (new.documento, new.fecha_ing, new.motivo, new.envio, 2, new.destino, new.recepcion, new.observacion, new.recibido)
  RETURNING seguimiento_pase.idpase, seguimiento_pase.documento, seguimiento_pase.fecha_ing, seguimiento_pase.motivo, seguimiento_pase.envio, seguimiento_pase.origen, seguimiento_pase.destino, seguimiento_pase.recepcion, seguimiento_pase.observacion, seguimiento_pase.recibido;


CREATE OR REPLACE RULE "_UPDATE" AS
    ON UPDATE TO vw_pase_tesoreria_s DO INSTEAD  UPDATE seguimiento_pase SET idpase = new.idpase, documento = new.documento, fecha_ing = new.fecha_ing, motivo = new.motivo, envio = new.envio, origen = new.origen, destino = new.destino, recepcion = new.recepcion, observacion = new.observacion, recibido = new.recibido
  WHERE seguimiento_pase.destino = 2 AND seguimiento_pase.idpase = old.idpase;