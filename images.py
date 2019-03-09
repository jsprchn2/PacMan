import pygame


class ImageSupervisor:

    def __init__(self, image, sheet=False, position_offset=None, resize=None, key=None,
                 convert=True, transparency=True, delay_animate=None, reversible=False, repeat=True):
        if not sheet:
            self.images = [pygame.image.load('images/' + image)]  # single image
        else:
            self.sheet = pygame.image.load('images/' + image)
            self.position_offset = position_offset  # get images from sprite sheet, using offsets
            self.images = self.extract_images()
        if resize:  # apply resizing
            self.images = [pygame.transform.scale(img, resize) for img in self.images]
        self.rect = self.images[0].get_rect()
        if convert:
            self.images = [image.convert() for image in self.images]
        if transparency:
            for i in self.images:
                i.set_colorkey((0, 0, 0, 0))
        if key:    # if keys provided, use keys instead of index value for getting images
            if not len(key) == len(self.images):
                raise ValueError('Must provide same number of keys as images')
            images_ref = dict()
            for k, i in zip(key, range(len(self.images))):
                images_ref[k] = self.images[i]
            self.images = images_ref
        else:
            self.image_index = 0
        self.delay_animate = delay_animate
        self.time_stamp = pygame.time.get_ticks()
        self.reversible = reversible
        self.repeat = repeat

    def flip(self, x_bool=True, y_bool=False):

        if isinstance(self.images, dict):
            self.images = {v: pygame.transform.flip(v, x_bool, y_bool) for k, v in self.images.items()}
        else:
            self.images = [pygame.transform.flip(x, x_bool, y_bool) for x in self.images]

    def get_image(self, key=None):

        if isinstance(self.images, list):
            return self.images[self.image_index], self.rect
        else:
            if not key:
                raise KeyError('No image key provided')
            return self.images[key], self.rect

    def all_images(self):

        return self.images

    def next_image(self):

        if not isinstance(self.images, list):
            raise ValueError('next_image not callable when using keys')
        if not self.repeat and self.image_index + 1 >= len(self.images):
            return self.images[self.image_index]
        if self.reversible and self.image_index + 1 >= len(self.images):
            self.images.reverse()
        if not self.delay_animate:
            self.image_index = (self.image_index + 1) % len(self.images)
        else:
            if abs(self.time_stamp - pygame.time.get_ticks()) > self.delay_animate:
                self.image_index = (self.image_index + 1) % len(self.images)
                self.time_stamp = pygame.time.get_ticks()

        return self.images[self.image_index]

    def extract_images(self):

        if not self.sheet:
            raise ValueError('Image manager has no sprite sheet to extract images from')
        result = []
        for rect in self.position_offset:
            select = pygame.Rect(rect)
            sub_image = pygame.Surface(select.size).convert(pygame.display.get_surface())
            sub_image.blit(self.sheet, (0, 0), select)
            result.append(sub_image)
        return result

