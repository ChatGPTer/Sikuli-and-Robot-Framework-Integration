import org.sikuli.basics.SikuliXforJython
#from sikuli import *
from sikuli import *
import org.sikuli.script.Region as SikuliRegion
from logger import *
import sys
import org.sikuli.script.FindFailed as FindFailed
from org.sikuli.script import Constants


# enable slow motion if debug log level enabled
if common.cfgLoggingLevel.lower() == 'debug':
    setShowActions(False)


# function for calling native sikuli methods
def sikuli_method(name, *args, **kwargs):
    return sys.modules['sikuli'].__dict__[name](*args, **kwargs)

# overwritten Region.exists method
def exists(target, timeout=0):
    addFoundImage(getFilename(target))
    return sikuli_method('exists', target, timeout)
    
# overwritten Region.find method    
def find(target):
    addFoundImage(getFilename(target))
    try:
        return sikuli_method('find',target)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e

# overwritten Region.findAll method    
def findAll(target):
    addFoundImage(getFilename(target))
    try:
        return sikuli_method('findAll',target)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e    

# overwritten Region.wait method    
def wait(target, timeout=None):
#    addFoundImage(getFilename(target))
#    return sikuli_method('wait', target, timeout)
    addFoundImage(getFilename(target))
    try:
        return sikuli_method('wait',target, timeout)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e  
     
# overwritten Region.waitVanish method 
def waitVanish(target, timeout=None):
    addFoundImage(getFilename(target))
    return sikuli_method('waitVanish',target,timeout)

#  overwritten Region.rightClick method    
def rightClick(target, modifiers=0):
    addFoundImage(getFilename(target))    
    try:
        return sikuli_method('rightClick',target,modifiers)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e    
 
#  overwritten Region.hover method      
def hover(target):
    addFoundImage(getFilename(target))    
    try:
        return sikuli_method('hover',target)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e    

## overwritten Region.type method   
#def type(*args):
#    addFoundImage(getFilename(*args))
#    try:
#        return sikuli_method('type',*args)
#    except FindFailed, e:            
#        BaseLogger.log.html_img("Find Filed", getFilename(*args))
#        BaseLogger.log.screenshot(msg="Region")
#        raise e    
#
## overwritten Region.paste method     
#def paste(*args):
#    addFoundImage(getFilename(*args))
#    try:
#        return sikuli_method('paste',*args)
#    except FindFailed, e:            
#        BaseLogger.log.html_img("Find Filed", getFilename(*args))
#        BaseLogger.log.screenshot(msg="Region")
#        raise e    


# overwritten Region.dragDrop method   
def dragDrop(src, dest, modifiers=0):
    addFoundImage(getFilename(src))
    addFoundImage(getFilename(dest))      
    try:
        return sikuli_method('dragDrop',src, dest, modifiers)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(src)+" or " + getFilename(src))
        BaseLogger.log.screenshot(msg="Region")
        raise e        

# overwritten Region.drag method       
def drag(target):
    addFoundImage(getFilename(target))    
    try:
        return sikuli_method('drag',target)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e   

# overwritten Region.dropAt method      
def dropAt(target, delay=None):
    addFoundImage(getFilename(target))    
    try:
        return sikuli_method('dropAt',target,delay)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e   

# overwritten Region.mouseMove method     
def mouseMove(target):
    addFoundImage(getFilename(target))    
    try:
        return sikuli_method('mouseMove',target)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e   
    
## overwritten Region.mouseMove method       
#def mouseDown(buttons):    
#    return sikuli_method('mouseDown',buttons)
#
## overwritten Region.mouseUp method
#def mouseUp(buttons=0):
#    return sikuli_method('mouseUp',buttons)
#
## overwritten Region.keyDown method
#def keyDown(keys):
#    return sikuli_method('keyDown',keys)   
#
## overwritten Region.keyUp method 
#def keyUp(keys=None): 
#    return sikuli_method('keyUp',keys)   
     
# overwritten Region.onAppear method  
def onAppear(target, handler): 
    addFoundImage(getFilename(target))    
    return sikuli_method('onAppear',target,handler)
  
    
# overwritten Region.onVanish method   
def onVanish(target, handler): 
    addFoundImage(getFilename(target))    
    return sikuli_method('onVanish',target,handler)
   
    
## overwritten Region.onChange method   
#def onChange(arg1, arg2=None):
#    return sikuli_method('onChange',arg1, arg2)    
#    
## overwritten Region.observe method    
#def observe(time=FOREVER, background=False):
#    return sikuli_method('observe',time, background)        
#    
## overwritten Region.setThrowException method        
#def setThrowException(flag):
#    return sikuli_method('setThrowException',flag)  
#
## overwritten Region.setAutoWaitTimeout method
#def setAutoWaitTimeout(sec):   
#    return sikuli_method('setAutoWaitTimeout',sec)  
            
# overwritten Region.click method  
def click(target,modifiers=0):
    addFoundImage(getFilename(target))
    try:
        return sikuli_method('click', target, modifiers)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e
    
# overwritten Region.click method  
def doubleclick(target,modifiers=0):
    addFoundImage(getFilename(target))
    try:
        return sikuli_method('doubleClick', target, modifiers)
    except FindFailed, e:            
        BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
        BaseLogger.log.screenshot(msg="Region")
        raise e  
    

   
    
# overwriten Sikuli Region class
class Region(SikuliRegion, BaseLogger):
    
    def click(self, target, modifiers=0):
        addFoundImage(getFilename(target))        
        try:
            return SikuliRegion.click(self, target, modifiers)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target))#"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e
    
    # overwritten Region.exists method    
    def exists(self, target, timeout=0.0):
        img = getFilename(target)
        reg = (self.getX(), self.getY(), self.getW(), self.getH())
        addFoundImage(img, reg)
        return SikuliRegion.exists(self, target, timeout)
    
#    # overwritten Region.find method    
#    def find(self,target):
#        try:
#            return SikuliRegion.find(self,target)
#        except FindFailed, e:            
#            self.log.html_img("Find Filed Region", getFilename(target))#"images/" + getFilename(target))
#            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
#            raise e
    
    # overwritten Region.findAll method    
    def findAll(self,target):
        addFoundImage(getFilename(target))
        try:
            return SikuliRegion.findAll(self,target)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e    
    
    # overwritten Region.wait method    
    def wait(self,target, timeout=0.0):
        addFoundImage(getFilename(target))
        try:
            return SikuliRegion.wait(self,target, timeout)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e  
         
    # overwritten Region.waitVanish method 
    def waitVanish(self,target, timeout=0.0):
        img = getFilename(target)
        reg = (self.getX(), self.getY(), self.getW(), self.getH())
        addFoundImage(img, reg)
        return SikuliRegion.waitVanish(self,target,timeout)
    
    #  overwritten Region.rightClick method    
    def rightClick(self,target, modifiers=0):  
        addFoundImage(getFilename(target))  
        try:
            return SikuliRegion.rightClick(self,target,modifiers)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e    
     
    #  overwritten Region.hover method      
    def hover(self,target): 
        addFoundImage(getFilename(target)) 
        try:
            return SikuliRegion.hover(self,target)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e    
    
#    # overwritten Region.type method   
#    def type(self,*args):
#        addFoundImage(getFilename(target))
#        try:
#            return SikuliRegion.type(self,*args)
#        except FindFailed, e:            
#            self.log.html_img("Find Filed",  getFilename(*args))
#            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
#            raise e    
#    
#    # overwritten Region.paste method     
#    def paste(self,*args):
#        try:
#            return SikuliRegion.paste(self,*args)
#        except FindFailed, e:            
#            self.log.html_img("Find Filed", getFilename(*args))
#            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
#            raise e    
    
    
    # overwritten Region.dragDrop method   
    def dragDrop(self,src, dest, modifiers=0):
        try:
            return SikuliRegion.dragDrop(self,src, dest, modifiers)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(src)+" or " + getFilename(src))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e        
    
    # overwritten Region.drag method       
    def drag(self,target): 
        addFoundImage(getFilename(target)) 
        try:
            return SikuliRegion.drag(self,target)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e   
    
    # overwritten Region.dropAt method      
    def dropAt(self,target, delay=0.0): 
        addFoundImage(getFilename(target))    
        try:
            return SikuliRegion.dropAt(self,target,delay)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e   
    
    # overwritten Region.mouseMove method     
    def mouseMove(self,target): 
        addFoundImage(getFilename(target))  
        try:
            return SikuliRegion.mouseMove(self,target)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e   
        
    # overwritten Region.mouseMove method       
    def mouseDown(self,buttons):    
        return SikuliRegion.mouseDown(self,buttons)
    
    # overwritten Region.mouseUp method
    def mouseUp(self,buttons=0):
        return SikuliRegion.mouseUp(self,buttons)
    
    # overwritten Region.keyDown method
    def keyDown(self,keys):
        return SikuliRegion.keyDown(self,keys)   
    
    # overwritten Region.keyUp method 
    def keyUp(self,keys=None): 
        return SikuliRegion.keyUp(self,keys)   
         
    # overwritten Region.onAppear method  
    def onAppear(self,target, handler): 
        img = getFilename(target)
        reg = (self.getX(), self.getY(), self.getW(), self.getH())
        addFoundImage(img, reg)   
        return SikuliRegion.onAppear(self,target,handler)
      
        
    # overwritten Region.onVanish method   
    def onVanish(self,target, handler): 
        img = getFilename(target)
        reg = (self.getX(), self.getY(), self.getW(), self.getH())
        addFoundImage(img, reg)   
        return SikuliRegion.onVanish(self,target,handler)
       
        
    # overwritten Region.onChange method   
    def onChange(self,arg1, arg2=None):
        return SikuliRegion.onChange(self,arg1, arg2)    
        
    # overwritten Region.observe method    
    def observe(self,time=Constants.FOREVER, background=False):
        return SikuliRegion.observe(self,time, background)        
        
    # overwritten Region.setThrowException method        
    def setThrowException(self,flag):
        return SikuliRegion.setThrowException(self,flag)  
    
    # overwritten Region.setAutoWaitTimeout method
    def setAutoWaitTimeout(self,sec):   
        return SikuliRegion.setAutoWaitTimeout(self,sec)  
                
    # overwritten Region.click method  
    #def click(self,target,modifiers=0):
    #   addFoundImage(getFilename(target))
    #    try:
    #       return sikuli_method('click', target, modifiers)
    #    except FindFailed, e:            
    #       BaseLogger.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
    #       self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
    #       raise e
        
    # overwritten Region.click method  
    def doubleclick(self,target,modifiers=0):
        addFoundImage(getFilename(target)) 
        try:
            return SikuliRegion.doubleClick(self, target, modifiers)
        except FindFailed, e:            
            self.log.html_img("Find Filed", getFilename(target)) #"images/" + getFilename(target))
            self.log.screenshot(msg="Region", region=(self.getX(), self.getY(), self.getW(), self.getH()))
            raise e  
