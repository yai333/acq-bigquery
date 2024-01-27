-- Create publication
CREATE PUBLICATION gcp_pub_cdc
FOR TABLE public.customers, public.orderdetails, 
          public.orders, public.products;

-- Create Publication slot
SELECT PG_CREATE_LOGICAL_REPLICATION_SLOT('gcp_pub_cdc_slot', 'pgoutput'); 


-- Create db user for Datastream
CREATE USER sys_datastream WITH ENCRYPTED PASSWORD 'xxxxxx';

-- Grant preivileges to the db user
GRANT RDS_REPLICATION TO sys_datastream;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO sys_datastream;
GRANT USAGE ON SCHEMA public TO sys_datastream;
ALTER DEFAULT PRIVILEGES IN SCHEMA public
  GRANT SELECT ON TABLES TO sys_datastream;