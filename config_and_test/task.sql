--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Debian 15.4-1.pgdg120+1)
-- Dumped by pg_dump version 15.4 (Debian 15.4-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: task; Type: SCHEMA; Schema: -; Owner: admin
--

CREATE SCHEMA task;
-- CREATE ROLE admin WITH SUPERUSER LOGIN;

ALTER SCHEMA task OWNER TO admin;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: account; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.account (
    id integer NOT NULL,
    client_id integer NOT NULL,
    type integer NOT NULL,
    account_no integer NOT NULL,
    is_active boolean NOT NULL,
    creation_date timestamp without time zone,
    last_modification_date timestamp without time zone
);


ALTER TABLE task.account OWNER TO admin;

--
-- Name: account_types; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.account_types (
    id integer NOT NULL,
    name character varying(50),
    description character varying(255)
);


ALTER TABLE task.account_types OWNER TO admin;

--
-- Name: customer; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.customer (
    id integer NOT NULL,
    name character varying(255),
    birth_date date,
    customer_no integer,
    is_active boolean,
    creation_date timestamp without time zone,
    last_modification_date timestamp without time zone,
    type integer NOT NULL
);


ALTER TABLE task.customer OWNER TO admin;

--
-- Name: customer_type; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.customer_type (
    id integer NOT NULL,
    name character varying(50),
    description character varying(255)
);


ALTER TABLE task.customer_type OWNER TO admin;

--
-- Name: smaple; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.smaple (
    id integer,
    amount integer,
    transaction_date timestamp without time zone,
    type_name character varying(50),
    account_number integer,
    customer_name character varying(255),
    destination_account_number integer,
    destination_customer_name character varying(255),
    destination_account_type_name character varying(50),
    credit boolean,
    is_juridical boolean
);


ALTER TABLE task.smaple OWNER TO admin;

--
-- Name: transaction; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.transaction (
    id integer NOT NULL,
    amount integer NOT NULL,
    transaction_date timestamp without time zone NOT NULL,
    type integer NOT NULL,
    from_account_id integer NOT NULL,
    to_account_id integer NOT NULL,
    credit boolean NOT NULL
);


ALTER TABLE task.transaction OWNER TO admin;

--
-- Name: transaction_type; Type: TABLE; Schema: task; Owner: admin
--

CREATE TABLE task.transaction_type (
    id integer NOT NULL,
    name character varying(50),
    description character varying(255)
);


ALTER TABLE task.transaction_type OWNER TO admin;

--
-- Data for Name: account; Type: TABLE DATA; Schema: task; Owner: admin
--




--
-- Data for Name: account_types; Type: TABLE DATA; Schema: task; Owner: admin
--




--
-- Data for Name: customer; Type: TABLE DATA; Schema: task; Owner: admin
--




--
-- Name: account account_pk; Type: CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.account
    ADD CONSTRAINT account_pk PRIMARY KEY (id);


--
-- Name: account_types account_types_pk; Type: CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.account_types
    ADD CONSTRAINT account_types_pk PRIMARY KEY (id);


--
-- Name: customer customer_pk; Type: CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.customer
    ADD CONSTRAINT customer_pk PRIMARY KEY (id);


--
-- Name: customer_type customer_type_pk; Type: CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.customer_type
    ADD CONSTRAINT customer_type_pk PRIMARY KEY (id);


--
-- Name: transaction transaction_pk; Type: CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.transaction
    ADD CONSTRAINT transaction_pk PRIMARY KEY (id);


--
-- Name: transaction_type transaction_type_pk; Type: CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.transaction_type
    ADD CONSTRAINT transaction_type_pk PRIMARY KEY (id);


--
-- Name: account account_account_types_id_fk; Type: FK CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.account
    ADD CONSTRAINT account_account_types_id_fk FOREIGN KEY (type) REFERENCES task.account_types(id);


--
-- Name: account account_customer_id_fk; Type: FK CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.account
    ADD CONSTRAINT account_customer_id_fk FOREIGN KEY (client_id) REFERENCES task.customer(id);


--
-- Name: customer customer_customer_type_id_fk; Type: FK CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.customer
    ADD CONSTRAINT customer_customer_type_id_fk FOREIGN KEY (type) REFERENCES task.customer_type(id);


--
-- Name: transaction transaction_account_id_fk; Type: FK CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.transaction
    ADD CONSTRAINT transaction_account_id_fk FOREIGN KEY (from_account_id) REFERENCES task.account(id);


--
-- Name: transaction transaction_account_id_fk2; Type: FK CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.transaction
    ADD CONSTRAINT transaction_account_id_fk2 FOREIGN KEY (to_account_id) REFERENCES task.account(id);


--
-- Name: transaction transaction_transaction_type_id_fk; Type: FK CONSTRAINT; Schema: task; Owner: admin
--

ALTER TABLE ONLY task.transaction
    ADD CONSTRAINT transaction_transaction_type_id_fk FOREIGN KEY (type) REFERENCES task.transaction_type(id);


--
-- PostgreSQL database dump complete
--

