FROM scratch

ADD 43a784386f93c50e6e7c7c408e94499688cab1bfb9b6023fc24d625554624c9b.tar.xz /
ADD 49e3e17efe6b2ff4e517eb9073389ea10a321806170c052947ca2d03f3bd84b2.tar.xz /
ADD 629e2400e7efb6d5895b6daaf0e011c1f943f93ab5323b82446d8e379544b8d5.tar.xz /
ADD 6a6b63980bfe115b2a8627711cc75abc157fe0b31bf7c047d773575d50d226b3.tar.xz /
ADD 6afbf436c211c26bfde475fe73a77b72e98f8e5add95c181ef29e74da0121c0c.tar.xz /
ADD 88fc811c851553f36fa1bd15d953804835feab46b4cdbd43c5655761b31fbece.tar.xz /

ENV LANG=en_US.UTF-8
ENV TZ=:/etc/localtime
ENV PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
ENV LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
ENV LAMBDA_TASK_ROOT=/var/task
ENV LAMBDA_RUNTIME_DIR=/var/runtime

WORKDIR /var/task

ENTRYPOINT ["/lambda-entrypoint.sh"]
