from pprint import pprint
from pprint import pformat
import os
import logging
# Default Configs for training
# NOTE that, config items could be overwriten by passing argument through command line.
# e.g. --voc-data-dir='./data/'

class Config:
    # data
    data_dir = ' '
    out_pred_dir = '/home/zhtang/water/txt/'
    out = 'predict'
    # for transfomers
    norm_mean = 0.0
    norm_std = 1.0

    # pretrained
    pretrained = None

    # architecture of network
    customize = True
    arch = 'waternet'

    train_num_workers = 8
    test_num_workers = 8

    # optimizers
    optim = 'SGD'
    use_adam = False

    # param for optimizer
    lr = 0.6
    weight_decay = 0.00005
    lr_decay = 0.33  #

    # record i-th log
    kind = '0'

    # set gpu :
    # gpu = True

    # visualization
    env = 'water-nn'  # visdom env
    port = 8097
    plot_every = 40  # vis every N iter

    # preset
    data = 'water'

    # training
    epoch = 120

    # if eval
    evaluate = False

    # debug
    # debug_file = '/tmp/debugf'

    test_num = 10000
    # model
    load_path = None
    save_path = '~/water/modelparams'
    labels_dict = (
    1036,
    1066,
    1064,
    1032,
    1004,
    1038,
    1040,
    1030,
    1014,
    1008,
    1002,
    1006,
    1078,
    1010,
    1046,
    1052,
    1056,
    1080,
    1060,
    1018,
    1020,
    1016,
    1022,
    1026,
    1042,
    1024,
    1028,
    1062,
    1044,
    1058,
    1048,
    1050,
    1034,
    1012
    )
    def _parse(self, kwargs):
        state_dict = self._state_dict()
        for k, v in kwargs.items():
            if k not in state_dict:
                raise ValueError('UnKnown Option: "--%s"' % k)
            setattr(self, k, v)

        print('======user config========')
        pprint(self._state_dict())
        print('==========end============')
        if opt.customize:
            logging_name = 'log' + '_self_' + opt.arch + '_'+ opt.optim + opt.kind + '.txt' 
        else:
            logging_name = 'log' + '_default_' + opt.arch  + '_' + opt.optim + opt.kind + '.txt'
        if not os.path.exists('log'):
            os.mkdir('log')

        logging_path = os.path.join('log', logging_name) 
    
        logging.basicConfig(level=logging.DEBUG,
                        filename=logging_path,
                        filemode='a',
                        format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                        datefmt='%H:%M:%S')
        logging.info('Logging for {}'.format(opt.arch))
        logging.info('======user config========')
        logging.info(pformat(self._state_dict()))
        logging.info('==========end============')
        # logging.info('optim : [{}], batch_size = {}, lr = {}, weight_decay= {}, momentum = {}'.format( \
        #                 args.optim, args.batch_size,
        #                 args.lr, args.weight_decay, args.momentum) )






    def _state_dict(self):
        return {k: getattr(self, k) for k, _ in Config.__dict__.items() \
                if not k.startswith('_')}
    

opt = Config()
