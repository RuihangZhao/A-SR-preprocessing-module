import argparse

parser = argparse.ArgumentParser(description="A SR preprocessing module")
parser.add_argument("--nEpochs", type=int, default=50, help="Number of epochs to train for")
parser.add_argument("--lr", type=float, default=0.1, help="Learning Rate. Default=0.1")
parser.add_argument("--step", type=int, default=10, help="Sets the learning rate to the initial LR decayed by momentum every n epochs, Default: n=10")
parser.add_argument("--cuda", action="store_true", help="Use cuda?")
parser.add_argument("--resume", default="",type=str, help="Path to checkpoint (default: none)")
parser.add_argument("--start-epoch", default=1, type=int, help="Manual epoch number (useful on restarts)")
parser.add_argument("--clip", type=float, default=0.4, help="Clipping Gradients. Default=0.4")
parser.add_argument("--threads", type=int, default=1, help="Number of threads for data loader to use, Default: 1")
parser.add_argument("--momentum", default=0.9, type=float, help="Momentum, Default: 0.9")
parser.add_argument("--weight-decay", "--wd", default=1e-4, type=float, help="Weight decay, Default: 1e-4")
parser.add_argument('--pretrained_SR', default='./checkpoint/model_FSRCNN_CNET_epoch_0.pth', type=str, help='path to pretrained model (default: none)')
parser.add_argument('--pretrained_TL', default='./TransferLearning/model_CNET_epoch_0.pth', type=str, help='path to pretrained model (default: none)')
parser.add_argument("--gpus", default="0", type=str, help="gpu ids (default: 0)")
parser.add_argument("--pretrained_SR_num", default=0, type=int, help="numbers of epochs that have been trained")
parser.add_argument("--pretrained_TL_num", default=0, type=int, help="numbers of epochs that have been trained")
parser.add_argument("--SRtrain", default=False, help="if train the super resolution network")
parser.add_argument("--TLtrain", default=True, help="if train the trainsfer learning network")
parser.add_argument("--SR_used", default=False, help="if use the SR method thought the pipeline")
parser.add_argument("--SRNet", default='FSRCNN', help='which network to use')

global opt
opt = parser.parse_args()