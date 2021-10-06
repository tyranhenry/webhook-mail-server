# Webhook Notification Email Server

An implementation of a server that can receive webhook notifications from Anchore and forward them to a list of email addresses, all running in an easy-to-deploy Docker container.

## Installation

Before getting started with the code, you will need to create a Gmail account that the server uses to send emails from. 

To allow the access, you need to set 'Less Secure App Access' settings in the google account.

To complete this setup, go to Google's Admin Console, and search for the Less Secure App setup. Ensure this is turned on as this is what will let the code make calls to the Gmail service, as it provides access from Python.

Clone this repository, and make the required changes to the code in `app.py` by updating all the occurrences of the text '<UPDATE VALUE>'.

If you already have a list of email addresses that you wish to have added to the email list, you can go ahead and add these to the `user_emails.txt` file, but ensure they are added as a list with nothing but the email address on each line, something like the below;

```
john.smith@anchore.com
aaron.richards@anchore.com
joe.bloggs@anchore.com
tom.daniels@anchore.com
admin@anchore.com
```

Once the code and text file have both been updated, you can build the container Dockerfile from your terminal. Make sure your terminal is in the directory of the cloned repo and then run;


```bash
docker build .
```

Once built, you can run the container on its own, or you can push it to Dockerhub(or any alternative repository) so that you can use the Kubernetes deployment method.

Once you have tagged and pushed the image to a repository, you can update the `deployment.yaml` so that the <UPDATE VALUE> is replaced with the repository link to the image you uploaded.

Save the .yaml file and then run;

```bash
kubectl create -f deployment.yaml
```

to deploy the server on Kubernetes.


## Usage

To add new emails to the list, you can send a POST request to the server with the email address as the payload.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)