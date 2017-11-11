#import "InputDetector.h"

@implementation InputDetector

// -----------------------------------
// Initialize the View
// -----------------------------------

- (id)initWithFrame:(NSRect)frame {
    self = [super initWithFrame:frame];
    if (!self) return nil;
    //[self allowedTouchTypes:YES];
    [self setWantsRestingTouches:YES];
    return self;
}

- (void)touchesBeganWithEvent:(NSEvent *)ev {
    NSSet *touches = [ev touchesMatchingPhase:NSTouchPhaseBegan inView:self];
    
    for (NSTouch *touch in touches) {
        /* Once you have a touch, getting the position is dead simple. */
        NSPoint fraction = touch.normalizedPosition;
        NSSize whole = touch.deviceSize;
        NSPoint wholeInches = {whole.width / 72.0, whole.height / 72.0};
        NSPoint pos = wholeInches;
        pos.x *= fraction.x;
        pos.y *= fraction.y;
        NSLog(@"%s: Finger is touching %g inches right and %g inches up "
              @"from lower left corner of trackpad.", __func__, pos.x, pos.y);
    }
}

@end



