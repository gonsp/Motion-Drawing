#import <Foundation/Foundation.h>
#import "InputDetector/InputDetector.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        NSRect frameRect = NSMakeRect(100, 100 , 256, 256);
        NSView* inputView = [[InputDetector alloc] initWithFrame:frameRect];
        [inputView setHidden:NO];
        [inputView setNeedsDisplay:YES];
        
        NSWindow *myWindow = [[NSWindow alloc] initWithContentRect:NSMakeRect(100,100,256,256) styleMask:NSWindowStyleMaskTitled backing:NSBackingStoreBuffered defer:NO];
        [myWindow setContentView:inputView];
    }
    return 0;
}
