# cloud_usage
A small repo which makes the training of pytorch model in azure possible

# How to use it in the training loop

```
# Instaniate a parser to get the paths to the remotely stored data

parser = argparse.ArgumentParser()
parser.add_argument('--data-path', type=str,
                      dest='data_path',
                      default='data',
                      help='data folder mounting point')

args = parser.parse_args()


# here the model is trained using data stored in the cloud and not on the local machine
# these paths can be used just like paths to the local device

train_folder = os.path.join(args.data_path, 'train')
val_folder = os.path.join(args.data_path, 'test')


# any pytorch model
# in my case I added the remote_run option, when the model is trained in the cloud. Then the data paths from previously configured parser are entered for the model to # #  # work with
model = EfficientNet(remote_run=True, train_path=train_folder, val_path=val_folder)

fit(model)

```
