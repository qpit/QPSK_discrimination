import numpy as np


def errorM(M,eta,visibility,dark,trysim,meanphotonmax):

    Error=[]
    for m in np.arange(0.1, meanphotonmax, 0.1):
        n=m*eta
        mean0 = dark / float(M) + 2 * n * (1 - visibility) / float(M)
        mean1 = dark / float(M) + 2 * n / float(M)
        mean2 = dark / float(M) + 2 * n * (1 + visibility) / float(M)
        p0 = np.exp(-mean0)
        p1 = np.exp(-mean1)
        p2 = np.exp(-mean2)

        suc=0

        suc0=0
        for trial in np.arange(trysim):

            outcomes=[]
            photon = np.random.poisson(mean0,1)
            if(photon==0):
                p0post=p0
                p1post=p1
                p2post=p2
                p3post=p1
            else:
                p0post=1-p0
                p1post=1-p1
                p2post=1-p2
                p3post=1-p1


            for stage in np.arange(M-1):
                if (p0post>=p1post and p0post>=p2post and p0post>=p3post):
                    photon = np.random.poisson(mean0, 1)
                    if(photon==0):
                        p0post=p0post*p0
                        p1post=p1post*p1
                        p2post=p2post*p2
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p0)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p2)
                        p3post=p3post*(1-p1)

                elif (p1post>=p2post and p1post>=p3post and p1post>p0post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p0
                        p2post=p2post*p1
                        p3post=p3post*p2
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p0)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p2)

                elif (p2post>=p3post and p2post>p0post and p2post>p1post):
                    photon = np.random.poisson(mean2, 1)
                    if(photon==0):
                        p0post=p0post*p2
                        p1post=p1post*p1
                        p2post=p2post*p0
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p2)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p0)
                        p3post=p3post*(1-p1)

                elif (p3post>p0post and p3post>p1post and p3post>p2post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p2
                        p2post=p2post*p1
                        p3post=p3post*p0
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p2)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p0)

            if (p0post>=p1post and p0post>=p2post and p0post>=p3post):
                suc0=suc0+1



        suc1=0
        for trial in np.arange(trysim):
            photon = np.random.poisson(mean1, 1)
            if(photon==0):
                p0post=p0
                p1post=p1
                p2post=p2
                p3post=p1
            else:
                p0post=1-p0
                p1post=1-p1
                p2post=1-p2
                p3post=1-p1

            for stage in np.arange(M-1):
                if (p0post>=p1post and p0post>=p2post and p0post>=p3post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p0
                        p1post=p1post*p1
                        p2post=p2post*p2
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p0)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p2)
                        p3post=p3post*(1-p1)
                elif (p1post>=p2post and p1post>=p3post and p1post>p0post):
                    photon = np.random.poisson(mean0, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p0
                        p2post=p2post*p1
                        p3post=p3post*p2
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p0)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p2)
                elif (p2post>=p3post and p2post>p0post and p2post>p1post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p2
                        p1post=p1post*p1
                        p2post=p2post*p0
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p2)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p0)
                        p3post=p3post*(1-p1)
                elif (p3post>p0post and p3post>p1post and p3post>p2post):
                    photon = np.random.poisson(mean2, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p2
                        p2post=p2post*p1
                        p3post=p3post*p0
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p2)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p0)

            if (p1post>=p2post and p1post>=p3post and p1post>p0post):
                suc1=suc1+1

        suc2=0
        for trial in np.arange(trysim):
            photon = np.random.poisson(mean2, 1)
            if(photon==0):
                p0post=p0
                p1post=p1
                p2post=p2
                p3post=p1
            else:
                p0post=1-p0
                p1post=1-p1
                p2post=1-p2
                p3post=1-p1

            for stage in np.arange(M-1):
                if (p0post>=p1post and p0post>=p2post and p0post>=p3post):
                    photon = np.random.poisson(mean2, 1)
                    if(photon==0):
                        p0post=p0post*p0
                        p1post=p1post*p1
                        p2post=p2post*p2
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p0)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p2)
                        p3post=p3post*(1-p1)

                elif (p1post>=p2post and p1post>=p3post and p1post>p0post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p0
                        p2post=p2post*p1
                        p3post=p3post*p2
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p0)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p2)
                elif (p2post>=p3post and p2post>p0post and p2post>p1post):
                    photon = np.random.poisson(mean0, 1)
                    if(photon==0):
                        p0post=p0post*p2
                        p1post=p1post*p1
                        p2post=p2post*p0
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p2)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p0)
                        p3post=p3post*(1-p1)
                elif (p3post>p0post and p3post>p1post and p3post>p2post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p2
                        p2post=p2post*p1
                        p3post=p3post*p0
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p2)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p0)

            if (p2post>=p3post and p2post>p0post and p2post>p1post):
                suc2=suc2+1

        suc3=0
        for trial in np.arange(trysim):
            photon = np.random.poisson(mean1, 1)
            if(photon==0):
                p0post=p0
                p1post=p1
                p2post=p2
                p3post=p1
            else:
                p0post=1-p0
                p1post=1-p1
                p2post=1-p2
                p3post=1-p1

            for stage in np.arange(M-1):
                if (p0post>=p1post and p0post>=p2post and p0post>=p3post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p0
                        p1post=p1post*p1
                        p2post=p2post*p2
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p0)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p2)
                        p3post=p3post*(1-p1)

                elif (p1post>=p2post and p1post>=p3post and p1post>p0post):
                    photon = np.random.poisson(mean2, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p0
                        p2post=p2post*p1
                        p3post=p3post*p2
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p0)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p2)
                elif (p2post>=p3post and p2post>p0post and p2post>p1post):
                    photon = np.random.poisson(mean1, 1)
                    if(photon==0):
                        p0post=p0post*p2
                        p1post=p1post*p1
                        p2post=p2post*p0
                        p3post=p3post*p1
                    else:
                        p0post=p0post*(1-p2)
                        p1post=p1post*(1-p1)
                        p2post=p2post*(1-p0)
                        p3post=p3post*(1-p1)
                elif (p3post>p0post and p3post>p1post and p3post>p2post):
                    photon = np.random.poisson(mean0, 1)
                    if(photon==0):
                        p0post=p0post*p1
                        p1post=p1post*p2
                        p2post=p2post*p1
                        p3post=p3post*p0
                    else:
                        p0post=p0post*(1-p1)
                        p1post=p1post*(1-p2)
                        p2post=p2post*(1-p1)
                        p3post=p3post*(1-p0)

            if (p3post>p2post and p3post>p0post and p3post>p1post):
                suc3=suc3+1

        suc=(suc0/float(trysim)+suc1/float(trysim)+suc2/float(trysim)+suc3/float(trysim))/float(4)+suc
        error=1-suc
        Error+=[error]

    return Error
