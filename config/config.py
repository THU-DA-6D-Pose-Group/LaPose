from __future__ import print_function

import absl.flags as flags

flags.DEFINE_string("semantic_encoder_name", 'psp_net', 'select a backbone')

# datasets
flags.DEFINE_integer('obj_c', 6, 'number of categories')
flags.DEFINE_string('dataset', 'CAMERA+Real', 'Real CAMERA or CAMERA+Real')
flags.DEFINE_string('dataset_dir', '', 'path to the dataset')
flags.DEFINE_float('syn_ratio', 3, 'CAMERA data ratio if CAMERA+Real')
flags.DEFINE_string('per_obj', 'all', 'only train an specified object')
flags.DEFINE_integer('ban_mug', 0, 'not include mug if true')
flags.DEFINE_float('DZI_PAD_SCALE', 1.5, '')
flags.DEFINE_string('DZI_TYPE', 'uniform', '')
flags.DEFINE_float('DZI_SCALE_RATIO', 0.25, '')
flags.DEFINE_float('DZI_SHIFT_RATIO', 0.25, '')

# input parameters
flags.DEFINE_integer("img_size", 256, 'size of the cropped image')
flags.DEFINE_integer("out_res", 64, 'size of output nocs')
flags.DEFINE_string("mask_attention_type", 'concat', 'for pnpnet')
flags.DEFINE_integer("dino_img_size", 448, 'size of the cropped image')

# data aug parameters
flags.DEFINE_integer('roi_mask_r', 3, 'radius for mask aug')
flags.DEFINE_float('roi_mask_pro', 0.5, 'probability to augment mask')
flags.DEFINE_float('aug_pc_pro', 0.2, 'probability to augment pc')
flags.DEFINE_float('aug_pc_r', 0.002, 'change 2mm on pc')
flags.DEFINE_float('aug_rt_pro', 0.3, 'probability to augment rt')
flags.DEFINE_float('aug_bb_pro', 0.3, 'probability to augment size')
flags.DEFINE_float('aug_bc_pro', 0.3, 'box cage based augmentation, only valid for bowl, mug')

# rgb aug
flags.DEFINE_string('color_aug_type', 'new', 'cosy+aae')
flags.DEFINE_float('color_aug_prob', 0.8, '')
flags.DEFINE_string('color_aug_code', '', '')
flags.DEFINE_bool('COLOR_AUG_SYN_ONLY', False, '')

flags.DEFINE_integer('feat_ts', 128, 'translation / scale feature channel')
flags.DEFINE_float('use_pnp', -1, 'whether use pnp')

flags.DEFINE_integer("num_workers", 8, "cpu cores for loading dataset")
flags.DEFINE_integer('batch_size', 40, '')
flags.DEFINE_integer('total_epoch', 150, 'total epoches in training')
flags.DEFINE_integer('train_size', 16000, 'number of images in each epoch')
# #####################space is not enough, trade time for space####################
flags.DEFINE_integer('accumulate', 1, '')   # the real batch size is batchsize x accumulate
#

# for different losses
flags.DEFINE_string('pose_loss_type', 'l1', 'l1 or smoothl1')
flags.DEFINE_bool('add_diff_loss', False, 'add diff loss')
flags.DEFINE_float('rot_1_w', 1, '')
flags.DEFINE_float('tran_w', 1, '')
flags.DEFINE_float('size_w', 1, '')
flags.DEFINE_float('scale_w', 2, '')
flags.DEFINE_float('prop_pm_w', 1, '')
flags.DEFINE_float('coor_w', 0.1, '')
flags.DEFINE_float('con_w', -1, '')

# # training parameters
# # learning rate scheduler
flags.DEFINE_float('lr', 1e-3, '')
flags.DEFINE_float('lr_pose', 1.0, '')
flags.DEFINE_integer('lr_decay_iters', 50, '')  # some parameter for the scheduler
# ### optimizer  ####
flags.DEFINE_string('lr_scheduler_name', 'flat_and_anneal', 'linear/warm_flat_anneal/')
flags.DEFINE_string('anneal_method', 'cosine', '')
flags.DEFINE_float('anneal_point', 0.72, '')
flags.DEFINE_string('optimizer_type', 'Ranger', '[Ranger|Adam]')
flags.DEFINE_float('weight_decay', 0.01, '')
flags.DEFINE_float('warmup_factor', 0.001, '')
flags.DEFINE_integer('warmup_iters', 100, '')
flags.DEFINE_string('warmup_method', 'linear', '')
flags.DEFINE_float('gamma', 0.1, '')
flags.DEFINE_float('poly_power', 0.9, '')
#
# # save parameters
flags.DEFINE_integer('save_every', 10, '')  # save models every 'save_every' epoch
flags.DEFINE_integer('log_every', 100, 'save log file every 100 iterations')
flags.DEFINE_string('model_save', 'output/modelsave', 'path to save checkpoint')
# # resume
flags.DEFINE_bool('resume', False, '1 for resume, 0 for training from the start')
flags.DEFINE_string('resume_model', '', 'path to the saved model')
flags.DEFINE_integer('resume_point', 0, 'the epoch to continue the training')

###################for evaluation#################
flags.DEFINE_integer('eval_refine_mug', 1, 'refine mug when evaluation')
flags.DEFINE_integer('eval_visualize_pcl', 0, 'save pcl when evaluation')
flags.DEFINE_integer('eval_inference_only', 0, 'inference without evaluation')
flags.DEFINE_integer('eval_precise', 0, '')
flags.DEFINE_bool('real_iou', True, 'use correct iou')
flags.DEFINE_bool('use_match_for_pose', True, 'use iou match for pose')
flags.DEFINE_string('result_dir', None, 'results of other method')
flags.DEFINE_integer('eval_batch_size', 1, '')

flags.DEFINE_integer('mask_dim', 1, '1:mask a vector totally| 3:mask every coordinate')

#
flags.DEFINE_bool('dinov2', True, 'whether use dino feature')
flags.DEFINE_bool('pnp_att_mask', True, 'whether use attention mask in pnp head')
flags.DEFINE_bool('mask_input', False, 'whether use mask for rgb input')
flags.DEFINE_string('att_thr_type', 'value', 'attention threshold type')
flags.DEFINE_float('att_thr', 0.3, 'attention threshold')
flags.DEFINE_float('att_ratio_thr', 0.5, 'attention threshold')
flags.DEFINE_bool('use_uncertainty_loss', False, 'whether uncertainty loss for NOCS')
flags.DEFINE_bool('use_consistency_loss', False, 'whether consistency loss for NOCS and pose')
flags.DEFINE_float('con_threshold', 10, '')
flags.DEFINE_bool('att_use_dino', False, 'whether use attention mask in pnp head')
flags.DEFINE_string('coor_type', 'both', 'convnext, dino, both')
flags.DEFINE_bool('att_use_rgb', True, 'whether use attention mask in pnp head')
flags.DEFINE_string('coor_gt_sym', 'rot', 'rot / coor / radius')
flags.DEFINE_integer('rot_sym_num', 30, 'how many rotation for symmetry')
flags.DEFINE_integer('log_var_min', -10, 'minimum log var')
flags.DEFINE_string('att_type', 'var', 'mask / var')
flags.DEFINE_string('uncertain_type', 'la', 'la| ga')
flags.DEFINE_bool('pre_norm', True, '')
flags.DEFINE_bool('use_bbox_hw',True,'')


# scale_net config
flags.DEFINE_bool('use_hw', True, 'whether input hw in last layer')
flags.DEFINE_integer('feat_dim', 24, '')
flags.DEFINE_string('backbone', 'mobilenetv3s', '')
flags.DEFINE_bool('use_scale_net', False, 'whether use scale net?')
flags.DEFINE_string('sn_path','', 'the path of scale net model')