import subprocess

def generate(name,f):
    s='cd ../output & ffmpeg -start_number 1 -r '+str(f)+' -i '+str(name)+'-frame_'+str(f)+'_%d.jpg -vcodec libx264 '+str(name)+'_Output_'+str(f)+'.mp4'
    #p=subprocess.call('ffmpeg -start_number 1 -r 5 -i V_1-frame%d.jpg -vcodec mpeg4 V_1_Output.avi',shell=True)
    p = subprocess.call(s, shell=True)
    import shutil
    newPath= shutil.copy('C:/Users/Bipin Gowda/PycharmProjects/GodsEye/output/'+name+'_Output_'+str(f)+'.mp4','C:/Users/Bipin Gowda/PycharmProjects/GodsEye/api/media/output')

