# Generated by Django 4.2.19 on 2025-02-23 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='item_image',
            field=models.CharField(default='https://www.google.com/imgres?q=placeholder%20food%20image&imgurl=https%3A%2F%2Fcdn.vectorstock.com%2Fi%2F500p%2F42%2F11%2Fcreative-concept-of-brain-food-symbolized-vector-53434211.jpg&imgrefurl=https%3A%2F%2Fwww.vectorstock.com%2Froyalty-free-vectors%2Ffood-placeholder-vectors&docid=DTuB0awS6s_LNM&tbnid=k6ci5Bta0fB66M&vet=12ahUKEwiXjfq9gtqLAxUDD1kFHWZmA3AQM3oECGUQAA..i&w=660&h=500&hcb=2&ved=2ahUKEwiXjfq9gtqLAxUDD1kFHWZmA3AQM3oECGUQAA', max_length=500),
        ),
    ]
