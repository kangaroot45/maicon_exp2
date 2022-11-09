import os

'''
Pretrained Model accessible through: models/trainer.py Line 313: self._load_checkpoint()

Dataset accessible through: datasets/CD_dataset.py Line 107(A), 108(B), 111(label)
                            self.root_dir, self.img_name_list[index % self.A_size]
                            root_dir from data_config.py

Chooses dataset from below: data_name
                            "AI-HUB" -> 'D:/Developments/Dataset/AI-HUB/splitted/'
                            "AI-HUB_Sq" -> 'D:/Developments/Dataset/AI-HUB_Sq/'
                            "AI-HUB_Sq_Shadow' -> 'D:/Developments/Dataset/AI-HUB_Sq_Shadow/'

                            * test & val data not used yet!
'''

if __name__ == "__main__":
    gpus = 0

    version = "Original"

    checkpoint_root=f"C:/Users/Navy/Desktop/MAICON/{version}/checkpoints/"
    vis_root=f"C:/Users/Navy/Desktop/MAICON/{version}/vis/"
    data_name=f"MAICON_{version}"

    img_size=256
    batch_size=16
    lr=0.0001
    max_epochs=200
    embed_dim=256

    n_class = 4

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

    arguments = f"--img_size {img_size} --loss {loss} --checkpoint_root {checkpoint_root} --vis_root {vis_root} --lr_policy {lr_policy} --optimizer {optimizer} --pretrain {pretrain} --split {split} --split_val {split_val} --net_G {net_G} --multi_scale_train {multi_scale_train} --multi_scale_infer {multi_scale_infer} --gpu_ids {gpus} --max_epochs {max_epochs} --project_name {project_name} --batch_size {batch_size} --shuffle_AB {shuffle_AB} --data_name {data_name}  --lr {lr} --embed_dim {embed_dim} --n_class {n_class}"
    os.system(f'python D:/Developments/ChangeFormer/main_cd.py {arguments}')

    #Specify GPU to use (only for multiple GPUs)
    #CUDA_VISIBLE_DEVICES=0

