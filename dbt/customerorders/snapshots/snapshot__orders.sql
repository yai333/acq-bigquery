{% snapshot snapshot__orders %}

{{
    config(
      target_schema='snapshots_customerorders',
      unique_key='orderid',
      strategy='check',
      invalidate_hard_deletes=True,
      check_cols=['orderdate', 'customerid', 'totalamount'],
    )
}}

SELECT * FROM {{ source('customerorders', 'orders') }}

{% endsnapshot %}