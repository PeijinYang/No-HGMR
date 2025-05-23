'''
Created on Oct 10, 2018
Tensorflow Implementation of Neural Graph Collaborative Filtering (NGCF) model in:
Wang Xiang et al. Neural Graph Collaborative Filtering. In SIGIR 2019.

@author: Xiang Wang (xiangwang@u.nus.edu)
'''
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Run NoHGMR.")
    parser.add_argument('--weights_path', nargs='?', default='',
                        help='Store model path.')
    parser.add_argument('--data_path', nargs='?', default='../Data/',
                        help='Input data path.')
    parser.add_argument('--proj_path', nargs='?', default='',
                        help='Project path.')

    parser.add_argument('--dataset', nargs='?', default='Beibei',
                        help='Choose a dataset from {Beibei,Taobao}')
    parser.add_argument('--pretrain', type=int, default=0,
                        help='0: No pretrain, -1: Pretrain with the learned embeddings, 1:Pretrain with stored models.')
    parser.add_argument('--verbose', type=int, default=1,
                        help='Interval of evaluation.')
    parser.add_argument('--is_norm', type=int, default=1,
                    help='Interval of evaluation.')
    parser.add_argument('--epoch', type=int, default=500,
                        help='Number of epoch.')

    parser.add_argument('--embed_size', type=int, default=64,   #common parameter
                        help='Embedding size.')
    parser.add_argument('--layer_size', nargs='?', default='[64,64, 64, 64]', #common parameter
                        help='Output sizes of every layer')
    parser.add_argument('--batch_size', type=int, default=1024,
                        help='Batch size.')

    parser.add_argument('--regs', nargs='?', default='[1e-5,1e-5,1e-2]',   # not used in GHCF
                        help='Regularizations.')
    parser.add_argument('--lr', type=float, default=0.001,   #common parameter
                        help='Learning rate.')

    parser.add_argument('--model_type', nargs='?', default='NoHGMR',
                        help='Specify the name of model (NoGMR).')
    parser.add_argument('--adj_type', nargs='?', default='pre',
                        help='Specify the type of the adjacency (laplacian) matrix from {plain, norm, mean}.')
    parser.add_argument('--alg_type', nargs='?', default='lightgcn',
                        help='Specify the type of the graph convolutional layer from {ngcf, gcn, gcmc}.')

    parser.add_argument('--gpu_id', type=int, default=1,
                        help='Gpu id')

    parser.add_argument('--node_dropout_flag', type=int, default=1,
                        help='0: Disable node dropout, 1: Activate node dropout')
    parser.add_argument('--node_dropout', nargs='?', default='[0.1]',
                        help='Keep probability w.r.t. node dropout (i.e., 1-dropout_ratio) for each deep layer. 1: no dropout.')

    parser.add_argument('--Ks', nargs='?', default='[10, 50, 100]',
                        help='K for Top-K list')

    parser.add_argument('--save_flag', type=int, default=0,
                        help='0: Disable model saver, 1: Activate model saver')

    parser.add_argument('--test_flag', nargs='?', default='part',
                        help='Specify the test type from {part, full}, indicating whether the reference is done in mini-batch')

    parser.add_argument('--report', type=int, default=0,
                        help='0: Disable performance report w.r.t. sparsity levels, 1: Show performance report w.r.t. sparsity levels')


    #GHCF parameters

    parser.add_argument('--wid', nargs='?', default='[0.0005,0.0007,0.001]',
                        help='negative weight, [0.001,0.05,0.1] or [0.001,0.05, 0.1] for beibei, [0.0005,0.0007,0.001] for taobao')

    parser.add_argument('--decay', type=float, default=0.1,
                        help='Regularization, 10 for beibei, 0.1 for taobao')

    parser.add_argument('--coefficient', nargs='?', default='[1/6, 4/6, 1/6]',
                        help='Regularization, [0.0/6, 5.0/6, 1.0/6] or [1.0/6, 4.0/6, 1.0/6] for beibei, [1.0/6, 4.0/6, 1.0/6] for taobao')

    parser.add_argument('--mess_dropout', nargs='?', default='[0.2]',
                        help='Keep probability w.r.t. message dropout, 0.2 for beibei and taobao')




    return parser.parse_args()
