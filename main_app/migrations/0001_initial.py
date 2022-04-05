from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('licenseNumber', models.CharField(max_length=12)),
                ('phoneNumber', models.CharField(max_length=12)),
                ('email', models.EmailField(max_length=254)),
                ('isAgent', models.BooleanField(default=True)),
                ('isAdmin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='RealEstate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('province', models.CharField(choices=[('Ontario', 'Ontario'), ('Prince Edward Island', 'Prince Edward Island'), ('Nova Scotia', 'Nova Scotia'), ('New Brunswick', 'New Brunswick'), ('Newfoundland and Labrador', 'Newfoundland and Labrador'), ('Quebec', 'Quebec'), ('Winnipeg', 'Winnipeg'), ('Saskatchewan', 'Saskatchewan'), ('Alberta', 'Alberta'), ('British Columbia', 'British Columbia'), ('Yukon', 'Yukon'), ('Northwest Territories', 'Northwest Territories'), ('Nunavut', 'Nunavut')], default='Ontario', max_length=50)),
                ('city', models.CharField(max_length=20)),
                ('address', models.TextField(max_length=250)),
                ('postalCode', models.CharField(max_length=7)),
                ('price', models.IntegerField()),
                ('buildingType', models.CharField(choices=[('C', 'Condo'), ('T', 'Townhouse'), ('S', 'Semi-Detached'), ('H', 'House')], default='C', max_length=1)),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.IntegerField()),
                ('parking', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1)),
                ('sqft', models.IntegerField()),
                ('listingDate', models.DateField(verbose_name='Listing Date')),
                ('closingDate', models.DateField(verbose_name='Closing Date')),
                ('description', models.CharField(max_length=2500)),
                ('isPublished', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=1)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ProfilePhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ListingPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=200)),
                ('real_estate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.realestate')),
            ],
        ),
    ]
