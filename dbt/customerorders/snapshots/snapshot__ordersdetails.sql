{% snapshot snapshot__orderdetails %}

{{
    config(
      target_schema='snapshots_customerorders',
      unique_key='orderdetailid',
      strategy='check',
      invalidate_hard_deletes=True,
      check_cols=['orderid', 'productid', 'quantity'],
    )
}}

SELECT * FROM {{ source('customerorders', 'orderdetails') }}

{% endsnapshot %}