{% snapshot snapshot__products %}

{{
    config(
      target_schema='snapshots_customerorders',
      unique_key='productid',
      strategy='check',
      invalidate_hard_deletes=True,
      check_cols=['name','price'],
    )
}}

SELECT * FROM {{ source('customerorders', 'products') }}

{% endsnapshot %}