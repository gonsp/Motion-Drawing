#ifndef InputDetector_h
#define InputDetector_h

#import <Cocoa/Cocoa.h>

@interface InputDetector : NSView {
    int x_size;
    int y_size;
}

- (id)initWithFrame:(NSRect)frame;

- (void)refresh:(CGPoint)pos;

- (void)send:(CGPoint)pos;

@end


#endif /* InputDetector_h */
