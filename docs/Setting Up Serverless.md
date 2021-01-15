# Setting up a serverless deploy

This document is a work in progress. For more information, contact Jordan M (@j6k4m8).

Note that there is already an official serverless deploy running! If you are interested in running your own, you can check out the following information. But you most likely do not need to make a new deploy if you are working on the "main" genderbias team deploy.

## 0. Install dependencies

```shell
pip3 install -r ./requirements.txt
```

From this directory, you should also install zappa:

```shell
pip3 install zappa
```

## 1. Create a new zappa deploy

```shell
zappa init
```

Follow the prompts. Then, add `"slim_handler": true` to the new `zappa_settings.json` file.

## 2. Deploy the Lambda

```shell
zappa deploy
```

This will take a long time! You will need to upload >80MB.

## 3. You're ready!

To push updates, run `zappa update`.
