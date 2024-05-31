# Example Django application for CloudBees Feature Management

This application demonstrates how you can integrate CloudBees Feature Management with your Djangoapplication.
The application shows how your React application can respond live to changes in feature flag settings - when you update flag values in the CloudBees platform the display will update within moments.

## Insert your SDK Key

Every application using CloudBees Feature Management needs to be configured with an SDK Key that connects it to your Flags & configurations in the [CloudBees Platform](https://cloudbees.io/).
You can retrieve your SDK Key for a particular Environment by visiting _Feature Management -> Installation_.
Then, replace the placeholder in `demo/fm_init.py` with your SDK Key:

`sdk_key = '<INSERT YOUR SDK KEY HERE>'`

For example:

`sdkKey = '9f8564ba-05a2-48b2-8735-70beb585a24a'`

## Run the application

Configure and activate a virtual environment for the application.

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the application's dependencies.

```bash
pip install -r requirements.txt
```

Run the application locally

```bash
python manage.py runserver 8080
```

...then visit the provided URL.

## Feature flags

The application uses the following feature flags:

- `showMessage`

A **boolean** flag that turns the message on or off.

- `message`

A **string** flag that sets the message text.

- `fontSize`

A **int** flag that sets the font size. The flag has options for 12, 16, or 24 px text size.

- `fontColor`

A **string** flag that sets the font color. The flag has options for red, green, or blue text color.

## Modifying flag values

Login to the [CloudBees platform](https://cloudbees.io/) and vist the _Feature Management_ section.
If you have configured your SDK Key correctly you should see the above flags have been created.
Change the value of one of these flags then save, ensuring the _Configuration status_ is _On_.
The application's page will automatically update shortly after to reflect the new flag value(s).

For more information on setting flag values, see the [CloudBees Feature Management documentation](https://docs.cloudbees.io/docs/cloudbees-feature-management/latest/).
