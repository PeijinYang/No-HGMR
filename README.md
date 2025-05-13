## Reproducibility

```
parser.add_argument('--wid', nargs='?', default='[0.1,0.1,0.1]',
                        help='negative weight, [0.1,0.1,0.1] for beibei, [0.01,0.01,0.01] for taobao')
parser.add_argument('--decay', type=float, default=10,
                        help='Regularization, 10 for beibei, 0.01 for taobao')
parser.add_argument('--coefficient', nargs='?', default='[0.0/6, 5.0/6, 1.0/6]',
                        help='Regularization, [0.0/6, 5.0/6, 1.0/6] for beibei, [1.0/6, 4.0/6, 1.0/6] for taobao')
parser.add_argument('--mess_dropout', nargs='?', default='[0.2]',
                        help='Keep probability w.r.t. message dropout, 0.2 for beibei and taobao')
```

## Suggestions for parameters

Several important parameters need to be tuned for different datasets, which are:

```
parser.add_argument('--wid', nargs='?', default='[0.1,0.1,0.1]',
                        help='negative weight, [0.1,0.1,0.1] for beibei, [0.01,0.01,0.01] for taobao')
parser.add_argument('--decay', type=float, default=10,
                        help='Regularization, 10 for beibei, 0.01 for taobao')
parser.add_argument('--coefficient', nargs='?', default='[0.0/6, 5.0/6, 1.0/6]',
                        help='Regularization, [0.0/6, 5.0/6, 1.0/6] for beibei, [1.0/6, 4.0/6, 1.0/6] for taobao')
parser.add_argument('--mess_dropout', nargs='?', default='[0.2]',
                        help='Keep probability w.r.t. message dropout, 0.2 for beibei and taobao')
```

Specifically, we suggest to tune "wid" among \[0.001,0.005,0.01,0.02,0.05,0.1,0.2,0.5]. It's also acceptable to simply make the three weights the same, e.g., self.weight = \[0.1, 0.1, 0.1] or self.weight = \[0.01, 0.01, 0.01]. Generally, this parameter is related to the sparsity of dataset. If the dataset is more sparse, then a small value of negative_weight may lead to a better performance.

The coefficient parameter determines the importance of different tasks in multi-task learning. In our datasets, there are three loss coefﬁcients λ 1 , λ 2 , and λ 3 . As λ 1 + λ 2 + λ 3 = 1, when λ 1 and λ 2 are given, the value of λ 3 is determined. We suggest to tune the three coefﬁcients in \[0, 1/6, 2/6, 3/6, 4/6, 5/6, 1].






