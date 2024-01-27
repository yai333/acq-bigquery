{% snapshot snapshot__customers %}

{{
    config(
      target_schema='snapshots_customerorders',
      unique_key='customerid',
      strategy='check',
      invalidate_hard_deletes=True,
      check_cols=['name', 'email', 'country'],
    )
}}

SELECT * FROM {{ source('customerorders', 'customers') }}

{% endsnapshot %}