#import "InputDetector.h"

@implementation InputDetector

// -----------------------------------
// Initialize the View
// -----------------------------------

- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    [self setAllowedTouchTypes:YES];
    NSLog(@"%lu", (unsigned long)[self allowedTouchTypes]);
    [self setWantsRestingTouches:YES];
    [self becomeFirstResponder];
    [self setWantsRestingTouches:YES];
    return self;
}

- (void)touchesBeganWithEvent:(NSEvent *)event {
    NSSet *touches = [event touchesMatchingPhase:NSTouchPhaseBegan inView:self];
    for(NSTouch *touch in touches) {
        NSPoint normalizedPosition = touch.normalizedPosition;
        
        //points inside `normalizedPosition`
        //top center: (.5, 1), bottom left: (1, 0)
    }
    NSLog(@"HELLOOOO");
}
- (void)touchesMovedWithEvent:(NSEvent *)event {
    NSLog(@"HELLOOOO");
}

- (void)touchesEndedWithEvent:(NSEvent *)event {
    NSLog(@"HELLOOOO");

}
- (void)touchesCancelledWithEvent:(NSEvent *)event {
    NSLog(@"HELLOOOO");
}

- (void)pressureChangeWithEvent:(NSEvent *)event {
    //NSLog(@"Pressure changed");
}

-(void)mouseDown:(NSEvent *)theEvent {
    NSLog(@"MouseDown in NSView");
}

@end



