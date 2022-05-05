INSERT INTO "CNG_STTE_CODE" (ID, CODE, DESCRIPTION, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_STTE_CODE"'), 'S01', 'Selangor', 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_STTE_CODE" (ID, CODE, DESCRIPTION, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_STTE_CODE"'), 'S02', 'Negeri Sembilan', 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_STTE_CODE" (ID, CODE, DESCRIPTION, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_STTE_CODE"'), 'S03', 'Melaka', 1,1, CURRENT_TIMESTAMP);

INSERT INTO "CNG_VENU" (ID, CODE, DESCRIPTION, VENUE_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_VENU"'), 'V01', 'Dewan Melur', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_VENU" (ID, CODE, description, VENUE_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_VENU"'), 'V02', 'Dewan Kenanga', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_VENU" (ID, CODE, DESCRIPTION, VENUE_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_VENU"'), 'V03', 'Bilik Mesyuarat I', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_VENU" (ID, CODE, DESCRIPTION, VENUE_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_VENU"'), 'V04', 'Bilik Mesyuarat II', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_VENU" (ID, CODE, DESCRIPTION, VENUE_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_VENU"'), 'V05', 'Bilik Mesyuarat III', 1, 1,1, CURRENT_TIMESTAMP);


-- CUSTOMER
INSERT INTO "CNG_ACTR" (ID, IDENTITY_NO, NAME, ACTOR_TYPE, M_ST, C_ID, c_ts) values
(nextval('"SQ_CNG_ACTR"'), 'C01', 'Uda Baharum', 2, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_CSMR" (ID, ADDRESS) values
(currval('"SQ_CNG_ACTR"'), 'Jalan Jujur 1 Bandar Tun Razak, 56000 Cheras KL');
INSERT INTO "CNG_ACTR" (ID, IDENTITY_NO, NAME, ACTOR_TYPE, M_ST, C_ID, c_ts) values
(nextval('"SQ_CNG_ACTR"'), 'C02', 'Idora Khairi', 2, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_CSMR" (ID, ADDRESS) values
(currval('"SQ_CNG_ACTR"'), 'Jalan Jujur 1 Bandar Tun Razak, 56000 Cheras KL');


-- USER
INSERT INTO "CNG_PCPL" (ID, NAME, PRINCIPAL_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_PCPL"'), 'root', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_USER" (ID, REALNAME, EMAIL, PASSWORD) values
(currval('"SQ_CNG_PCPL"'), 'Root','root@gmail.com','abc123');
INSERT INTO "CNG_PCPL" (ID, NAME, PRINCIPAL_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_PCPL"'), 'sysadmin', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_USER" (ID, REALNAME, EMAIL, PASSWORD) values
(currval('"SQ_CNG_PCPL"'), 'Sysadmin','sysadmin@gmail.com','abc123');
INSERT INTO "CNG_PCPL" (ID, NAME, PRINCIPAL_TYPE, M_ST, C_ID, C_TS) values
(nextval('"SQ_CNG_PCPL"'),'uda.baharum', 1, 1,1, CURRENT_TIMESTAMP);
INSERT INTO "CNG_USER" (ID, REALNAME, EMAIL, PASSWORD) values
(currval('"SQ_CNG_PCPL"'), 'Uda','rafizan.baharum@gmail.com','abc123');


