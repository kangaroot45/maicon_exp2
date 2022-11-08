
class DataConfig:
    data_name = ""
    root_dir = ""
    label_transform = ""
    def get_data_config(self, data_name):
        self.data_name = data_name
        '''
        if data_name == 'LEVIR':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/Dataset/LEVIR-CD256/'
            #self.root_dir = 'D:/Developments/Dataset/LEVIR-CD/'
        elif data_name == 'DSIFN':
            self.label_transform = "norm"
            self.root_dir = '/media/lidan/ssd2/CDData/DSIFN_256/'
        elif data_name == 'WHU':
            self.label_transform = "norm"
            self.root_dir = '/media/lidan/ssd2/CDData/WHU-CD-256/'
        elif data_name == 'CDD':
            self.label_transform = "norm"
            self.root_dir = '/media/lidan/ssd2/CDData/CDD-CD-256/'
        elif data_name == 'TYPO':
            self.label_transform = "norm"
            self.root_dir = '/media/lidan/ssd2/CDData/TYPO/'
        elif data_name == 'quick_start_LEVIR':
            self.root_dir = './samples_LEVIR/'
        elif data_name == 'quick_start_DSIFN':
            self.root_dir = './samples_DSIFN/'
        elif data_name == 'AI-HUB':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/Dataset/AI-HUB/'
        elif data_name == 'AI-HUB_Shadow':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/AI-HUB_Results/Shadow/'
        '''
        if data_name == 'LEVIR':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/Dataset/LEVIR-CD256/'
        elif data_name == 'AI-HUB':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/Dataset/AI-HUB/splitted/'
        elif data_name == 'AI-HUB_Sq':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/Dataset/AI-HUB_Sq/'
        elif data_name == 'AI-HUB_Sq_Shadow':
            self.label_transform = "norm"
            self.root_dir = 'D:/Developments/Dataset/AI-HUB_Sq_Shadow/'
        elif data_name == 'AI-HUB_Sq_Hist':
            self.label_transform = "norm24"
            self.root_dir = 'D:/Developments/Dataset/AI-HUB_Sq_Hist/'
        elif data_name == 'AI-HUB_Multilabel':
            self.label_transform = "four"
            self.root_dir = 'C:/Users/Navy/Desktop/images/to256'
        else:
            raise TypeError('%s has not defined' % data_name)
        return self


if __name__ == '__main__':
    data = DataConfig().get_data_config(data_name='LEVIR')
    print(data.data_name)
    print(data.root_dir)
    print(data.label_transform)

