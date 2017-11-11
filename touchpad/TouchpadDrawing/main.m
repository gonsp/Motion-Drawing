#import <Foundation/Foundation.h>
#import "InputDetector/InputDetector.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        [NSApplication sharedApplication];
        NSUInteger windowStyle = NSWindowStyleMaskTitled | NSWindowStyleMaskClosable | NSWindowStyleMaskResizable;

        NSRect windowRect = NSMakeRect(100, 100, 400, 400);
        NSWindow* window = [[NSWindow alloc] initWithContentRect:windowRect
                                                        styleMask:windowStyle
                                                          backing:NSBackingStoreBuffered
                                                            defer:YES];
    
        NSView* inputView = [[InputDetector alloc] initWithFrame:windowRect];
        [inputView setHidden:YES];
        [inputView setNeedsDisplay:NO];
        [window setContentView:inputView];
        [window setAcceptsMouseMovedEvents:YES];

        [window makeKeyAndOrderFront:NSApp];
        
        NSLog(@"%hhd", [window acceptsMouseMovedEvents]);

        [NSApp run];
        
        NSLog(@"Closing touchpad input");
    }
    return 0;
}
