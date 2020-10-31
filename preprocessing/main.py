import click
from preprocessing import process


@click.command()
@click.argument('f_in', type=click.File('r'))
@click.argument('f_out', type=click.File('wb'))
def main(f_in, f_out):
    process(f_in, f_out)


if __name__ == '__main__':
    main()

