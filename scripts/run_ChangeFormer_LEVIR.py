import sys,runpy,os
import subprocess

'''
Pretrained Model accessible through: models/trainer.py Line 313: self._load_checkpoint()
'''

if __name__ == "__main__":
    gpus = 0
    checkpoint_root="D:/Developments/ChangeFormer/checkpoints/"
    vis_root="D:/Developments/ChangeFormer/vis/"
    data_name="LEVIR"

    img_size=256
    batch_size=16
    lr=0.0001
    max_epochs=200
    embed_dim=256

    net_G="ChangeFormerV6"

    lr_policy="linear"
    optimizer="adamw"
    loss="ce"
    multi_scale_train=True
    multi_scale_infer=False
    shuffle_AB=False

    pretrain="D:/Developments/ChangeFormer/pretrained/pretrained_changeformer.pt"

    split="train"
    split_val="test"
    project_name=f"CD_{net_G}_{data_name}_b{batch_size}_lr{lr}_{optimizer}_{split}_{split_val}_{max_epochs}_{lr_policy}_{loss}_multi_train_{multi_scale_train}_multi_infer_{multi_scale_infer}_shuffle_AB_{shuffle_AB}_embed_dim_{embed_dim}"

    #checkpoint_root += project_name
    #vis_root += project_name

    arguments = f"--img_size {img_size} --loss {loss} --checkpoint_root {checkpoint_root} --vis_root {vis_root} --lr_policy {lr_policy} --optimizer {optimizer} --pretrain {pretrain} --split {split} --split_val {split_val} --net_G {net_G} --multi_scale_train {multi_scale_train} --multi_scale_infer {multi_scale_infer} --gpu_ids {gpus} --max_epochs {max_epochs} --project_name {project_name} --batch_size {batch_size} --shuffle_AB {shuffle_AB} --data_name {data_name}  --lr {lr} --embed_dim {embed_dim}"
    #runpy.run_path('D:/Developments/ChangeFormer/main_cd.py', run_name="__main__")
    #subprocess.run(f'D:/Developments/ChangeFormer/main_cd.py {arguments}')
    os.system(f'python D:/Developments/ChangeFormer/main_cd.py {arguments}')

    #Specify GPU to use (only for multiple GPUs)
    #CUDA_VISIBLE_DEVICES=0

