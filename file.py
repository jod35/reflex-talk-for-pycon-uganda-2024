# Generated by Django 4.0.2 on 2024-01-28 09:57

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "username",
                    models.CharField(
                        error_messages={
                            "unique": "A user with that username already exists."
                        },
                        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                        max_length=150,
                        unique=True,
                        validators=[
                            django.contrib.auth.validators.UnicodeUsernameValidator()
                        ],
                        verbose_name="username",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(blank=True, max_length=100, null=True)),
                ("contact", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("nin", models.CharField(blank=True, max_length=20, null=True)),
                ("gender", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=255)),
                ("profile_photo", models.ImageField(upload_to="staff_photos/")),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("IND", "INDIVIDUAL"),
                            ("GRP", "GROUP"),
                            ("INS", "INSTITUSION"),
                        ],
                        max_length=100,
                        verbose_name="Client Type",
                    ),
                ),
                ("client_no", models.CharField(blank=True, max_length=100, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("email", models.CharField(blank=True, max_length=100, null=True)),
                ("contact", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "marital_status",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("occupation", models.CharField(blank=True, max_length=100, null=True)),
                ("dob", models.DateField(blank=True, null=True)),
                ("gender", models.CharField(blank=True, max_length=100, null=True)),
                ("date_joined", models.DateField(blank=True, null=True)),
                (
                    "next_of_kim",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "kim_contact",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("nin", models.CharField(blank=True, max_length=100, null=True)),
                ("address", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "descrioption",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "no_of_members",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("status", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.branch",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Branch",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("branch_code", models.CharField(blank=True, max_length=20, null=True)),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("location", models.CharField(blank=True, max_length=255, null=True)),
                ("staff", models.IntegerField(blank=True, null=True)),
                ("clients", models.IntegerField(blank=True, null=True)),
                ("opening_date", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("active", "Active"), ("inactive", "Inactive")],
                        max_length=10,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Company",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Company Name")),
                ("address", models.TextField(verbose_name="Address")),
                (
                    "company_logo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="company_logos/",
                        verbose_name="Company Logo",
                    ),
                ),
                (
                    "official_email",
                    models.EmailField(max_length=254, verbose_name="Official Email"),
                ),
                (
                    "contact_number",
                    models.CharField(max_length=30, verbose_name="Contact Number"),
                ),
                (
                    "website_url",
                    models.URLField(blank=True, null=True, verbose_name="Website URL"),
                ),
                (
                    "contact_person",
                    models.CharField(max_length=255, verbose_name="Contact Person"),
                ),
                (
                    "phone_number",
                    models.CharField(max_length=30, verbose_name="Phone Number"),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[("A", "Active"), ("I", "Inactive")],
                        max_length=2,
                        null=True,
                        verbose_name="Company Status",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Companies",
            },
        ),
        migrations.CreateModel(
            name="CreditReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(max_length=100)),
                ("national_id", models.CharField(max_length=20)),
                ("surname", models.CharField(max_length=100)),
                (
                    "filefield",
                    models.FileField(
                        blank=True, null=True, upload_to="credit_reports/"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Loan",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("contact", models.CharField(blank=True, max_length=15, null=True)),
                ("principal", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "interest_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "interest_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("loan_term", models.CharField(blank=True, max_length=100, null=True)),
                ("period", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("O", "Overdue"),
                            ("C", "cleared"),
                            ("A", "Active"),
                            ("W", "Written off"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Loan Status",
                    ),
                ),
                ("disbursement_date", models.DateField(blank=True, null=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "client",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Permissions",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Role",
                    models.CharField(
                        choices=[
                            ("A", "Admin"),
                            ("C", "Client"),
                            ("L", "Loan"),
                            ("R", "Reports"),
                        ],
                        max_length=2,
                        verbose_name="Role",
                    ),
                ),
                (
                    "choice",
                    models.CharField(
                        choices=[
                            ("admin_all_actions", "Perform all admin actions"),
                            ("admin", "Admin"),
                            ("client_add", "Add Clients"),
                            ("client_view", "View Clients"),
                            ("client_delete", "Delete Clients"),
                            ("client_edit", "Edit Clients"),
                            ("loan_add", "Add Loans"),
                            ("loan_delete", "Delete Loans"),
                            ("loan_view", "View Loans"),
                            ("loan_approve", "Approve Loans"),
                            ("loan_process", "Process Loan disbursements"),
                            ("report_add", "Add Reports"),
                            ("report_delete", "Delete Reports"),
                            ("report_view", "View Reports"),
                        ],
                        max_length=50,
                        verbose_name="choice",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UploadedPDF",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("pdf_file", models.FileField(upload_to="uploaded_pdfs/")),
            ],
        ),
        migrations.CreateModel(
            name="Roles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.branch",
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.company",
                    ),
                ),
                (
                    "permissions",
                    models.ManyToManyField(blank=True, to="app.Permissions"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Repayments",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("contact", models.CharField(blank=True, max_length=15, null=True)),
                ("principal", models.CharField(blank=True, max_length=100, null=True)),
                ("payment", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "amount_paid",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "remaining_amount",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                (
                    "mode_of_Payment",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("payment_date", models.DateField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.client",
                    ),
                ),
                (
                    "loan",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.loan",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewStaff",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("contact", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("nin", models.CharField(blank=True, max_length=20, null=True)),
                ("gender", models.CharField(max_length=10)),
                ("address", models.CharField(max_length=255)),
                ("profile_photo", models.ImageField(upload_to="staff_photos/")),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.branch",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.roles",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewFee",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fee_name", models.CharField(max_length=100)),
                ("fee_type", models.CharField(max_length=50)),
                (
                    "fee_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("fee_varies", models.IntegerField(blank=True, null=True)),
                ("payment_type", models.CharField(max_length=20)),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.branch",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoanProduct",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("number_of_loans", models.IntegerField(blank=True, null=True)),
                (
                    "interest_method",
                    models.CharField(blank=True, max_length=20, null=True),
                ),
                (
                    "rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("has_fees", models.BooleanField(blank=True, default=False, null=True)),
                ("loan_fees", models.CharField(blank=True, max_length=10, null=True)),
                ("penalty", models.CharField(blank=True, max_length=10, null=True)),
                (
                    "penalty_interest_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("grace_period", models.IntegerField(blank=True, null=True)),
                (
                    "interest_amount_per_annum",
                    models.IntegerField(blank=True, null=True),
                ),
                ("frequency", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "branch",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.branch",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="LoanDisbursements",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("principal", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "interest_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "interest_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("loan_term", models.CharField(blank=True, max_length=100, null=True)),
                ("period", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("O", "Overdue"),
                            ("C", "cleared"),
                            ("A", "Active"),
                            ("W", "Written off"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Loan Status",
                    ),
                ),
                (
                    "mode_of_transfer",
                    models.CharField(
                        blank=True,
                        choices=[("B", "Bank"), ("C", "Cash")],
                        max_length=100,
                        null=True,
                        verbose_name="Mode of Transfer",
                    ),
                ),
                ("disbursement_date", models.DateField(blank=True, null=True)),
                ("due_date", models.DateField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "client",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.client",
                    ),
                ),
                (
                    "loanproduct",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.loan",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="loan",
            name="loanproduct",
            field=models.ForeignKey(
                blank=True,
                default=None,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.loanproduct",
            ),
        ),
        migrations.CreateModel(
            name="Download",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("file", models.FileField(upload_to="downloads/")),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "created_report",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.creditreport",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="CollateralRegisterModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("client_alias", models.CharField(max_length=50)),
                ("item", models.CharField(max_length=50, verbose_name="Item")),
                (
                    "item_description",
                    models.CharField(
                        blank=True,
                        max_length=200,
                        null=True,
                        verbose_name="Description",
                    ),
                ),
                ("market_value", models.IntegerField(verbose_name="Market Value")),
                (
                    "forced_sale_value",
                    models.IntegerField(verbose_name="Forced Sale Value"),
                ),
                ("date_added", models.DateField(verbose_name="Date Added")),
                (
                    "attachment",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="collateralitem",
                        verbose_name="Attachment",
                    ),
                ),
                (
                    "client_name",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.client"
                    ),
                ),
                (
                    "loan_no",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="app.loan"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="branch",
            name="company",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.company"
            ),
        ),
        migrations.CreateModel(
            name="Application",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("contact", models.CharField(blank=True, max_length=15, null=True)),
                ("address", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "nin",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A", "Approved"),
                            ("P", "Pending"),
                            ("R", "Rejected"),
                            ("C", "Cancelled"),
                        ],
                        max_length=100,
                        null=True,
                        verbose_name="Application Status",
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "interest_rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                (
                    "purpose_of_funds",
                    models.CharField(blank=True, max_length=20, null=True, unique=True),
                ),
                (
                    "loan_term",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
                (
                    "reason_rejection",
                    models.CharField(blank=True, max_length=50, null=True, unique=True),
                ),
                ("period", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "rate",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=10, null=True
                    ),
                ),
                ("application_date", models.DateField(blank=True, null=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created_at",
                    ),
                ),
                (
                    "Branch",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.branch",
                    ),
                ),
                (
                    "client",
                    models.OneToOneField(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.client",
                    ),
                ),
                (
                    "loan",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.loan",
                    ),
                ),
                (
                    "loanproduct",
                    models.ForeignKey(
                        blank=True,
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.loanproduct",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="user",
            name="branch",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.branch",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="role",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.roles",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Permission",
                verbose_name="user permissions",
            ),
        ),
    ]
